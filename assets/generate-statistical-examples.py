#!/usr/bin/env python3
"""Generate ten original SVG examples with synthetic data and no dependencies.

Run: python3 generate.py
Assets and metadata are written beside this file, independent of the working
directory. Every displayed value comes from the data or calculations below.
"""
import html
import json
import math
import random
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RNG = random.Random(20261008)
BLUE = '#567F9C'
TEAL = '#659386'
CORAL = '#BA7D73'
GOLD = '#C39D5C'
GRAY = '#9099A1'
INK = '#27343E'
GRID = '#E3E8EB'
WIDTH, HEIGHT = 900, 610
X0, Y0, PW, PH = 110, 125, 670, 335
LICENSE = 'PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0'
METADATA = []


def text(x, y, label, size=18, anchor='start', color=INK, rotate=None):
    rotation = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ''
    return (f'<text x="{x:.3f}" y="{y:.3f}" font-size="{size}" '
            f'text-anchor="{anchor}" fill="{color}"{rotation}>'
            f'{html.escape(str(label))}</text>')


def line(x1, y1, x2, y2, color=GRID, width=1.2, dash=None):
    pattern = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" '
            f'y2="{y2:.3f}" stroke="{color}" stroke-width="{width}"{pattern}/>')


def circle(x, y, radius=5, color=BLUE, opacity=1):
    return (f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{radius}" '
            f'fill="{color}" fill-opacity="{opacity}"/>')


def path(points, color=BLUE, width=3, fill='none', opacity=1, close=False, dash=None):
    commands = 'M ' + ' L '.join(f'{x:.3f},{y:.3f}' for x, y in points)
    if close:
        commands += ' Z'
    pattern = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="{commands}" stroke="{color}" stroke-width="{width}" '
            f'fill="{fill}" fill-opacity="{opacity}"{pattern}/>')


def canvas(title):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" '
            f'height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" '
            'role="img" aria-labelledby="title desc">',
            '<title id="title">' + html.escape(title) + '</title>',
            '<desc id="desc">Synthetic example. Not paper results. '
            'Reproducible using the accompanying Python source.</desc>',
            '<rect width="100%" height="100%" fill="white"/>',
            '<g font-family="Arial, Helvetica, sans-serif">',
            text(45, 42, title, 25),
            text(45, 72, 'Synthetic example / Not paper results', 18, color=CORAL)]


def axes(svg, xmin, xmax, ymin, ymax, xticks, yticks, xlabel, ylabel):
    px = lambda value: X0 + PW * (value - xmin) / (xmax - xmin)
    py = lambda value: Y0 + PH - PH * (value - ymin) / (ymax - ymin)
    for value in yticks:
        svg.append(line(X0, py(value), X0 + PW, py(value)))
        svg.append(text(X0 - 13, py(value) + 6, f'{value:g}', 16, 'end'))
    for value in xticks:
        svg.append(line(px(value), Y0 + PH, px(value), Y0 + PH + 6, INK))
        svg.append(text(px(value), Y0 + PH + 27, f'{value:g}', 16, 'middle'))
    svg.extend([line(X0, Y0, X0, Y0 + PH, INK, 1.7),
                line(X0, Y0 + PH, X0 + PW, Y0 + PH, INK, 1.7),
                text(X0 + PW / 2, Y0 + PH + 66, xlabel, 18, 'middle'),
                text(30, Y0 + PH / 2, ylabel, 18, 'middle', rotate=-90)])
    return px, py


def legend(svg, entries, x=110, y=106):
    for label, color in entries:
        svg.append(line(x, y - 6, x + 25, y - 6, color, 4))
        svg.append(text(x + 34, y, label, 16))
        x += 32 + 9.5 * len(label) + 30


def save(svg, file_name, notes):
    for number, note in enumerate(notes):
        svg.append(text(45, 558 + 21 * number, note, 14))
    svg += ['</g>', '</svg>']
    (ROOT / file_name).write_text('\n'.join(svg) + '\n', encoding='utf-8')


def describe(identifier, topic, title, asset, zh, en, analysis, details=None):
    item = dict(id=identifier, topic=topic, title=title, asset=asset, zh=zh,
                en=en, analysis_zh=analysis, license=LICENSE,
                source_title='可复现教学绘图代码',
                source_url='assets/generate-statistical-examples.py')
    if details:
        item['calculation'] = details
    METADATA.append(item)


def percentile(values, probability):
    ordered = sorted(values)
    position = probability * (len(ordered) - 1)
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def jacobi_eigen(matrix):
    """Diagonalize a real symmetric matrix using Jacobi rotations."""
    n = len(matrix)
    values = [row[:] for row in matrix]
    vectors = [[float(i == j) for j in range(n)] for i in range(n)]
    for _ in range(100):
        p, q = max(((i, j) for i in range(n) for j in range(i + 1, n)),
                   key=lambda pair: abs(values[pair[0]][pair[1]]))
        if abs(values[p][q]) < 1e-12:
            break
        angle = 0.5 * math.atan2(2 * values[p][q], values[q][q] - values[p][p])
        c, s = math.cos(angle), math.sin(angle)
        app, aqq, apq = values[p][p], values[q][q], values[p][q]
        for k in range(n):
            if k not in (p, q):
                akp, akq = values[k][p], values[k][q]
                values[k][p] = values[p][k] = c * akp - s * akq
                values[k][q] = values[q][k] = s * akp + c * akq
        values[p][p] = c * c * app - 2 * s * c * apq + s * s * aqq
        values[q][q] = s * s * app + 2 * s * c * apq + c * c * aqq
        values[p][q] = values[q][p] = 0.0
        for k in range(n):
            vkp, vkq = vectors[k][p], vectors[k][q]
            vectors[k][p] = c * vkp - s * vkq
            vectors[k][q] = s * vkp + c * vkq
    order = sorted(range(n), key=lambda i: values[i][i], reverse=True)
    return ([values[i][i] for i in order],
            [[vectors[k][i] for k in range(n)] for i in order])


def generate():
    samples = [[RNG.gauss(-0.3, 0.8) for _ in range(100)],
               [RNG.gauss(0.8, 0.6) for _ in range(100)]]
    bandwidth = 0.4
    svg = canvas('KDE: read density, not cumulative probability')
    px, py = axes(svg, -3, 4, 0, 0.7, [-3, -2, -1, 0, 1, 2, 3, 4],
                  [0, 0.2, 0.4, 0.6], 'Synthetic score (arbitrary units)',
                  'Probability density (1 / score unit)')
    legend(svg, [('Group A', BLUE), ('Group B', TEAL)])
    for sample, color in zip(samples, [BLUE, TEAL]):
        points = []
        for i in range(181):
            x = -3 + 7 * i / 180
            density = sum(math.exp(-0.5 * ((x - v) / bandwidth) ** 2)
                          for v in sample) / (len(sample) * bandwidth * math.sqrt(2 * math.pi))
            points.append((px(x), py(density)))
        svg.append(path([(px(-3), py(0))] + points + [(px(4), py(0))],
                        color, 0, color, 0.12, True))
        svg.append(path(points, color))
    save(svg, 'kde.svg', ['Gaussian kernel; n = 100 per group; bandwidth = 0.4 score units.',
                         'Shading is area under the density curve, not a confidence interval.'])
    describe('teaching-kde', 'KDE 密度分布', 'KDE：看哪里密集，不是已经累计了多少',
             'kde.svg', '同一坐标对照两组模拟分数，曲线越高说明该处更密集；浅色填充只是曲线下面积。',
             'The two synthetic groups share axes; taller curves indicate greater local density, and shading marks area under the curve.',
             ['每组100个模拟样本，使用高斯核和0.4的固定带宽；纵轴是密度。',
              '曲线面积约为1，曲线高度不是累计比例；阴影不代表置信区间。'],
             {'kernel': 'Gaussian', 'bandwidth': bandwidth, 'n_per_group': 100})

    svg = canvas('ECDF: read the fraction at or below a value')
    px, py = axes(svg, -3, 4, 0, 1, [-3, -2, -1, 0, 1, 2, 3, 4],
                  [0, 0.25, 0.5, 0.75, 1], 'Synthetic score (arbitrary units)',
                  'Cumulative fraction')
    legend(svg, [('Group A', BLUE), ('Group B', TEAL)])
    for sample, color in zip(samples, [BLUE, TEAL]):
        points = [(px(-3), py(0))]
        for i, value in enumerate(sorted(sample), 1):
            points += [(px(value), py((i - 1) / len(sample))),
                       (px(value), py(i / len(sample)))]
        points.append((px(4), py(1)))
        svg.append(path(points, color, 2.7))
    save(svg, 'ecdf.svg', ['ECDF = number of observed scores at or below x, divided by n.',
                          'Uses the same 100 synthetic samples per group as the KDE example.'])
    describe('teaching-ecdf', 'ECDF 累计分布', 'ECDF：直接读有多少样本不超过这个值',
             'ecdf.svg', '阶梯线在每个样本处上升，纵轴是已累计的样本比例；不用把平滑密度误认成覆盖率。',
             'Each observed score raises the step curve, and the vertical axis shows the cumulative sample fraction.',
             ['与KDE使用同一批模拟样本，累计比例按样本计数直接计算。',
              '在某个阈值比较两条线，读的是不超过阈值的比例，不是该处密度。'])

    records, groups = [], []
    for group in [0, 1]:
        for _ in range(40):
            base = RNG.gauss(-0.8 if group == 0 else 0.8, 0.9)
            records.append([base + RNG.gauss(0, 0.4),
                            0.7 * base + RNG.gauss(0, 0.7),
                            -0.3 * base + RNG.gauss(0, 0.8)])
            groups.append(group)
    means = [statistics.mean(row[j] for row in records) for j in range(3)]
    scales = [statistics.stdev(row[j] for row in records) for j in range(3)]
    standardized = [[(row[j] - means[j]) / scales[j] for j in range(3)]
                    for row in records]
    covariance = [[sum(row[i] * row[j] for row in standardized) / 79
                   for j in range(3)] for i in range(3)]
    eigenvalues, vectors = jacobi_eigen(covariance)
    proportions = [v / sum(eigenvalues) for v in eigenvalues]
    assert abs(sum(proportions) - 1) < 1e-10 and min(eigenvalues) >= 0
    for value, vector in zip(eigenvalues, vectors):
        residual = [sum(covariance[i][j] * vector[j] for j in range(3))
                    - value * vector[i] for i in range(3)]
        assert max(map(abs, residual)) < 1e-8
    projections = [[sum(row[j] * vectors[k][j] for j in range(3))
                    for k in range(2)] for row in standardized]
    svg = canvas('PCA: project standardized features, then explain the axes')
    px, py = axes(svg, -4, 4, -3, 3, [-4, -2, 0, 2, 4], [-3, -2, -1, 0, 1, 2, 3],
                  f'PC1 ({100 * proportions[0]:.1f}% explained variance)',
                  f'PC2 ({100 * proportions[1]:.1f}% explained variance)')
    legend(svg, [('Group A', BLUE), ('Group B', TEAL)])
    for point, group in zip(projections, groups):
        svg.append(circle(px(point[0]), py(point[1]), 4.8, [BLUE, TEAL][group], 0.75))
    save(svg, 'pca.svg', ['80 synthetic observations; 3 features centered and scaled by sample standard deviation.',
                         'PCA uses the sample covariance eigensystem. A projection is not a generalization test.'])
    describe('teaching-pca', 'PCA / 空间嵌入', 'PCA：先定义输入，再看二维投影',
             'pca.svg', '两组模拟样本的三个标准化特征投到前两主成分，轴上直接给真实计算的解释方差。',
             'Three standardized features from two synthetic groups are projected onto the first two principal components, with computed explained variance on the axes.',
             ['80个样本，三维特征先中心化，再除以样本标准差；主成分由协方差矩阵求得。',
              '颜色是原分组，PCA没有使用分组训练；分得开不等于分类准确或泛化成立。'],
             {'n': 80, 'features': 3, 'standardization_ddof': 1,
              'eigenvalues': eigenvalues, 'explained_variance_ratio': proportions})

    svg = canvas('Radar: compare profiles on explicitly normalized axes')
    cx, cy, radius = 410, 300, 168
    labels = ['Coverage', 'Recall', 'Precision', 'Consistency', 'Recovery']
    angles = [-math.pi / 2 + i * 2 * math.pi / 5 for i in range(5)]
    for fraction in [0.25, 0.5, 0.75, 1]:
        vertices = [(cx + radius * fraction * math.cos(a),
                     cy + radius * fraction * math.sin(a)) for a in angles]
        svg.append(path(vertices, GRID, 1.2, close=True))
        svg.append(text(cx + 8, cy - radius * fraction + 6, f'{fraction:g}', 14))
    for a, label in zip(angles, labels):
        svg.append(line(cx, cy, cx + radius * math.cos(a), cy + radius * math.sin(a)))
        svg.append(text(cx + (radius + 48) * math.cos(a),
                        cy + (radius + 26) * math.sin(a) + 6, label, 17, 'middle'))
    profiles = [[0.72, 0.66, 0.80, 0.70, 0.64], [0.80, 0.76, 0.77, 0.82, 0.69]]
    legend(svg, [('Profile A', BLUE), ('Profile B', TEAL)], x=595)
    for profile, color in zip(profiles, [BLUE, TEAL]):
        vertices = [(cx + radius * value * math.cos(a),
                     cy + radius * value * math.sin(a))
                    for a, value in zip(angles, profile)]
        svg.append(path(vertices, color, 2.7, color, 0.12, True))
        svg += [circle(x, y, 4, color) for x, y in vertices]
    save(svg, 'radar.svg', ['All axes use synthetic normalized scores from 0 to 1; higher is better.',
                           'Compare individual axes. Filled polygon area is not a validated overall score.'])
    describe('teaching-radar', '雷达与多指标', '雷达：看各项轮廓，别拿面积当总分',
             'radar.svg', '每根轴都是越高越好的0到1模拟分数，颜色贯穿点和线；逐项比较，比比较整块面积更有意义。',
             'Every axis is a synthetic 0–1 score with higher values preferred; consistent point and line colors support axis-by-axis comparisons.',
             ['各轴同尺度、同方向，中心是0，外圈是1；真实图必须先说明如何归一化。',
              '这张图没有定义综合分数，不能把多边形面积当作经过验证的总能力。'])

    observations = [[RNG.gauss(40 + 5 * setting, 9) for _ in range(40)]
                    for setting in range(6)]
    intervals, averages = [], []
    for values in observations:
        averages.append(statistics.mean(values))
        means_boot = [statistics.mean(RNG.choices(values, k=40)) for _ in range(1000)]
        intervals.append([percentile(means_boot, p) for p in [0.025, 0.16, 0.84, 0.975]])
    svg = canvas('Bootstrap intervals: identify the resampled unit')
    px, py = axes(svg, 0, 5, 25, 80, list(range(6)), [30, 40, 50, 60, 70, 80],
                  'Ordered synthetic setting', 'Mean synthetic response (arbitrary units)')
    legend(svg, [('Mean', BLUE), ('Inner: 68%', TEAL), ('Outer: 95%', GRAY)])
    for low, high, color, opacity in [(0, 3, GRAY, 0.14), (1, 2, TEAL, 0.30)]:
        points = [(px(i), py(bounds[low])) for i, bounds in enumerate(intervals)]
        points += [(px(i), py(intervals[i][high])) for i in range(5, -1, -1)]
        svg.append(path(points, color, 0, color, opacity, True))
    svg.append(path([(px(i), py(value)) for i, value in enumerate(averages)], BLUE))
    svg += [circle(px(i), py(value), 4.5, BLUE) for i, value in enumerate(averages)]
    save(svg, 'confidence.svg', ['40 independent synthetic observations per setting; 1,000 bootstrap resamples per setting.',
                                'Pointwise percentile intervals of the mean; connecting bands only guide the eye.'])
    describe('teaching-confidence', '置信带', '置信带：先认统计单位，再认内外两层',
             'confidence.svg', '深线是模拟样本均值，内层是68%、外层是95%的逐点bootstrap区间；宽度有计算依据，不是调个透明度。',
             'The line shows synthetic sample means; the inner and outer bands are computed 68% and 95% pointwise bootstrap percentile intervals.',
             ['每个设置有40个独立模拟观测，按观测有放回重采样1000次，再取均值分位数。',
              '区间针对各个均值，不是覆盖整个函数的同时置信带，也不表示样本本身落在带内。'],
             {'observations_per_setting': 40, 'bootstrap_resamples_per_setting': 1000,
              'interval_type': 'pointwise percentile bootstrap of mean',
              'levels': [0.68, 0.95], 'means': averages, 'bounds': intervals})

    baseline = [RNG.uniform(45, 88) for _ in range(24)]
    intervention = [min(100, max(0, value + RNG.gauss(5, 10))) for value in baseline]
    gains = [new - old for old, new in zip(baseline, intervention)]
    assert min(gains) > -30 and max(gains) < 35
    svg = canvas('Paired gains: keep each matched task together')
    px, py = axes(svg, -30, 35, 0, 25, [-30, -20, -10, 0, 10, 20, 30],
                  [1, 6, 12, 18, 24], 'Accuracy gain (percentage points)', 'Matched task ID')
    svg.append(line(px(0), Y0, px(0), Y0 + PH, GRAY, 1.7, '5 4'))
    for i, gain in enumerate(gains, 1):
        color = TEAL if gain >= 0 else CORAL
        svg.append(line(px(0), py(i), px(gain), py(i), color, 1.6))
        svg.append(circle(px(gain), py(i), 4.5, color))
    save(svg, 'paired-gain.svg', ['24 synthetic matched tasks; each dot is intervention accuracy minus baseline accuracy.',
                                 'The dashed zero line marks no gain. These task-level differences are not significance tests.'])
    describe('teaching-paired-gain', '配对增益', '配对增益：同一任务，直接看差了多少',
             'paired-gain.svg', '每点是一项模拟任务的干预减基线，零线右侧提高、左侧下降；既显示收益，也留下失败。',
             'Each point is the intervention-minus-baseline difference for a synthetic matched task; points right of zero improve, while points left of zero decline.',
             ['差值单位是百分点，不能写成相对百分比；每个任务保留自己的配对关系。',
              '散点显示任务差异，没有检验显著性，也没有替代总体汇总。'])

    matrix = [[68, 62, 74, 69, 70], [73, 66, 71, 72, 75], [76, None, 77, 73, 76]]
    svg = canvas('Heatmap: share one scale and show missing observations')
    left, top, cw, ch = 155, 150, 125, 82
    for j in range(5):
        svg.append(text(left + (j + 0.5) * cw, 132, f'Task {j + 1}', 18, 'middle'))
    for i, row in enumerate(matrix):
        svg.append(text(140, top + (i + 0.5) * ch + 6, f'Model {chr(65 + i)}', 17, 'end'))
        for j, value in enumerate(row):
            if value is None:
                fill, label = '#EBECEE', 'Missing'
            else:
                weight = (value - 60) / 20
                start, end = (242, 247, 249), (113, 155, 180)
                fill = '#%02x%02x%02x' % tuple(round(a + weight * (b - a)) for a, b in zip(start, end))
                label = f'{value}%'
            svg.append(f'<rect x="{left + j*cw}" y="{top + i*ch}" width="{cw}" height="{ch}" fill="{fill}" stroke="white" stroke-width="3"/>')
            svg.append(text(left + (j + 0.5) * cw, top + (i + 0.5) * ch + 6, label, 18, 'middle'))
    for k in range(101):
        weight = k / 100
        fill = '#%02x%02x%02x' % tuple(round(a + weight * (b - a)) for a, b in zip((242, 247, 249), (113, 155, 180)))
        svg.append(f'<rect x="{250+4*k}" y="445" width="4.1" height="18" fill="{fill}"/>')
    for value, x in [(60, 250), (70, 450), (80, 650)]:
        svg.append(text(x, 489, f'{value}%', 16, 'middle'))
    svg.append(text(450, 527, 'Synthetic accuracy (%)', 18, 'middle'))
    save(svg, 'heatmap.svg', ['All cells use the same 60% to 80% color scale; gray means no observation.',
                             'Synthetic values illustrate formatting only. Missing data are not replaced by zero.'])
    describe('teaching-heatmap', '热图', '热图：一个色标，缺测直接空出来',
             'heatmap.svg', '模型与任务交叉排，颜色和格内数值用同一尺度；缺测格单独写Missing，别伪装成零分。',
             'Models and tasks share one color scale with values printed in each cell; the missing observation is labeled separately rather than replaced by zero.',
             ['全图同一60%到80%色标，不能每行各自归一化后继续比较颜色。',
              '格内标数值，帮助读者在不辨色时仍能比较；灰色只表示缺测。'])

    costs, accuracies = [0.8, 1.8, 3.2, 5, 8.5, 12.5], [55, 64, 72, 74, 79, 78]
    svg = canvas('Cost and performance: identify actual configurations')
    px, py = axes(svg, 0, 14, 50, 85, [0, 2, 4, 6, 8, 10, 12, 14], [50, 60, 70, 80],
                  'Online cost per 1,000 queries (synthetic cost units)', 'Synthetic accuracy (%)')
    frontier = [i for i in range(6) if not any(costs[j] <= costs[i] and accuracies[j] >= accuracies[i]
                and (costs[j] < costs[i] or accuracies[j] > accuracies[i]) for j in range(6))]
    svg.append(path([(px(costs[i]), py(accuracies[i])) for i in frontier], TEAL, 2, dash='5 5'))
    for i, (cost, accuracy) in enumerate(zip(costs, accuracies)):
        svg.append(circle(px(cost), py(accuracy), 6, BLUE))
        svg.append(text(px(cost) + 10, py(accuracy) - 9, chr(65 + i), 16))
    save(svg, 'cost.svg', ['Dots are six synthetic configurations; dashed segments join non-dominated shown points only.',
                          'Cost covers online queries and excludes one-time training; no intermediate settings are implied.'])
    describe('teaching-cost', '成本性能图', '成本性能：每个点对应一项明确配置',
             'cost.svg', '横轴是模拟在线成本，纵轴是准确率，每个字母是一项配置；虚线只连接已画出的有效取舍点。',
             'Online cost and accuracy form the axes, and each letter identifies one synthetic configuration; dashed segments only connect the displayed non-dominated points.',
             ['成本按每1000次查询计，不混入一次性训练成本；真实图要另外报告后者。',
              '连接点是阅读辅助，不证明中间配置存在，也不代表连续最优函数。'])

    svg = canvas('Donut: show a composition with an explicit denominator')
    counts, colors = [40, 30, 20, 10], [BLUE, TEAL, GOLD, CORAL]
    total, circumference, offset = sum(counts), 2 * math.pi * 125, 0
    for count, color in zip(counts, colors):
        length = circumference * count / total
        svg.append(f'<circle cx="330" cy="310" r="125" fill="none" stroke="{color}" stroke-width="58" stroke-dasharray="{length:.6f} {circumference-length:.6f}" stroke-dashoffset="{-offset:.6f}" transform="rotate(-90 330 310)"/>')
        offset += length
    svg += [text(330, 305, 'n = 100', 24, 'middle'), text(330, 336, 'synthetic items', 16, 'middle')]
    for i, (count, color) in enumerate(zip(counts, colors)):
        svg.append(circle(590, 224 + 51 * i, 7, color))
        svg.append(text(610, 230 + 51 * i, f'Category {chr(65+i)}: {count} ({100*count/total:.0f}%)', 18))
    save(svg, 'donut.svg', ['100 synthetic items in four mutually exclusive categories; counts sum to the displayed total.',
                           'Percentages describe a composition, not joint associations between different variables.'])
    describe('teaching-donut', '饼图与环图', '环图：组成比例，先说总数',
             'donut.svg', '中心写100个模拟对象，旁边同时列数量和比例；四类互斥，所有扇区合起来才是一个整体。',
             'The center states 100 synthetic items and the legend lists counts and percentages; four mutually exclusive categories form the whole.',
             ['先给统计单位和分母，数量40、30、20、10真实相加为100。',
              '环图适合看构成；精确比较相近比例，数值或横向条图更直接。'])

    gains_x = [-4, 3, 7, 5, -2, -7, 1, 8]
    gains_y = [12, 8, -10, -4, -5, 15, -12, 4]
    svg = canvas('Two gains: separate improvement from trade-offs')
    px, py = axes(svg, -10, 10, -20, 20, [-10, -5, 0, 5, 10], [-20, -10, 0, 10, 20],
                  'Accuracy gain (percentage points)', 'Latency reduction (%)')
    svg.append(f'<rect x="{px(0)}" y="{py(20)}" width="{px(10)-px(0)}" height="{py(0)-py(20)}" fill="#E8F2ED"/>')
    svg.append(line(px(0), Y0, px(0), Y0 + PH, GRAY, 1.7, '5 4'))
    svg.append(line(X0, py(0), X0 + PW, py(0), GRAY, 1.7, '5 4'))
    svg.append(text(px(6), py(17), 'Both improve', 16, 'middle', TEAL))
    for i, (gx, gy) in enumerate(zip(gains_x, gains_y)):
        svg.append(circle(px(gx), py(gy), 5.5, BLUE))
        svg.append(text(px(gx) + 10, py(gy) - 8, chr(65 + i), 16))
    save(svg, 'two-gain.svg', ['Eight synthetic configurations. Positive latency reduction means faster responses.',
                              'Latency reduction = 100 × (baseline latency − new latency) / baseline latency.'])
    describe('teaching-two-gain', '二维增益', '二维增益：右上都改善，其他象限看取舍',
             'two-gain.svg', '准确率增益向右更好，延迟减少向上更好；零线分四区，右上是两项同时改善。',
             'Accuracy gains improve to the right and latency reduction improves upward; zero lines separate the quadrants, with joint improvements in the upper right.',
             ['横轴是百分点，纵轴是相对延迟减少百分比，两种单位明确分开。',
              '每个点是构造的配置，不是论文结果；落在哪个象限只说明这两项指标的关系。'])
    (ROOT / 'metadata.json').write_text(json.dumps(METADATA, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Generated {len(METADATA)} synthetic examples.')


if __name__ == '__main__':
    generate()
