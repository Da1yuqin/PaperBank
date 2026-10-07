#!/bin/sh
set -eu

# Run from any working directory. Only system tools are needed.
source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
project_dir=$(CDPATH= cd -- "$source_dir/.." && pwd)
output_dir="$source_dir/outputs"
app_dir="$output_dir/PaperBank Beagle.app"
resource_dir="$app_dir/Contents/Resources"
build_dir="$output_dir/.build"

if [ "$(uname -s)" != "Darwin" ]; then
    echo "This desktop companion builds on macOS only." >&2
    exit 1
fi
if ! /usr/bin/xcrun --find swiftc >/dev/null 2>&1; then
    echo "Swift compiler not found. Install Apple's Command Line Tools, then run this script again." >&2
    exit 1
fi
for asset in beagle-logo.png beagle-pet.png beagle-wave.gif; do
    if [ ! -f "$project_dir/assets/$asset" ]; then
        echo "Missing assets/$asset. Keep the complete PaperBank project together." >&2
        exit 1
    fi
done

mkdir -p "$build_dir" "$app_dir/Contents/MacOS" "$resource_dir"
sdk_dir=$(/usr/bin/xcrun --show-sdk-path)
for architecture in arm64 x86_64; do
    /usr/bin/xcrun swiftc "$source_dir/Main.swift" -O \
        -sdk "$sdk_dir" -target "$architecture-apple-macosx12.0" \
        -module-cache-path "$build_dir/module-cache" \
        -o "$build_dir/beagle-$architecture"
done
/usr/bin/lipo -create "$build_dir/beagle-arm64" "$build_dir/beagle-x86_64" \
    -output "$app_dir/Contents/MacOS/Beagle"
cp "$project_dir/assets/beagle-pet.png" "$project_dir/assets/beagle-wave.gif" "$resource_dir/"
cp "$project_dir/LICENSE" "$resource_dir/LICENSE"
icon_dir="$build_dir/Beagle.iconset"
mkdir -p "$icon_dir"
for dimension in 16 32 128 256 512; do
    /usr/bin/sips -z "$dimension" "$dimension" "$project_dir/assets/beagle-logo.png" \
        --out "$icon_dir/icon_${dimension}x${dimension}.png" >/dev/null
    doubled=$((dimension * 2))
    /usr/bin/sips -z "$doubled" "$doubled" "$project_dir/assets/beagle-logo.png" \
        --out "$icon_dir/icon_${dimension}x${dimension}@2x.png" >/dev/null
done
/usr/bin/iconutil -c icns -o "$resource_dir/Beagle.icns" "$icon_dir"

cat > "$app_dir/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>CFBundleExecutable</key><string>Beagle</string>
  <key>CFBundleIdentifier</key><string>io.github.da1yuqin.paperbank.beagle</string>
  <key>CFBundleName</key><string>PaperBank Beagle</string>
  <key>CFBundleDisplayName</key><string>PaperBank 贝果</string>
  <key>CFBundleIconFile</key><string>Beagle.icns</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleVersion</key><string>1</string>
  <key>CFBundleShortVersionString</key><string>1.0</string>
  <key>LSMinimumSystemVersion</key><string>12.0</string>
  <key>LSUIElement</key><true/>
  <key>NSHighResolutionCapable</key><true/>
</dict></plist>
PLIST

# Ad hoc signing makes the local bundle coherent; this is not Apple notarization.
/usr/bin/codesign --force --sign - "$app_dir"
package_dir="$build_dir/PaperBank-Beagle"
mkdir -p "$package_dir"
/usr/bin/ditto "$app_dir" "$package_dir/PaperBank Beagle.app"
cp "$source_dir/README.md" "$package_dir/README.md"
cp "$project_dir/LICENSE" "$package_dir/LICENSE"
/usr/bin/ditto -c -k --norsrc --noextattr --noqtn --keepParent "$package_dir" "$output_dir/PaperBank-Beagle-macOS.zip"
printf 'Built Universal macOS app: %s\n' "$app_dir"
printf 'Download archive: %s\n' "$output_dir/PaperBank-Beagle-macOS.zip"
