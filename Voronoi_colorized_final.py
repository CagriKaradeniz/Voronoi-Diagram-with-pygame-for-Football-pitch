import pygame, sys
import pandas as pd
from scipy.spatial import Voronoi
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial as spatial
import matplotlib.pyplot as plt
import matplotlib.path as path
import matplotlib as mpl
import shapely.geometry
from shapely.geometry import point
import Utils_cagri as util
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df = pd.read_csv('Tracking_data_home.csv',low_memory=False)
df1 = pd.read_csv('Tracking_data_away.csv',low_memory=False)
df.columns=df.columns.astype(int)
util.dataset_ozet(df)
df1.columns=df1.columns.astype(int)
util.dataset_ozet(df1)


PI = math.pi
pygame.init()

boyut = (1920, 1080)
font = pygame.font.SysFont("Helvetica", 48)
x_start = 170 * 1920 / 1280
y_start = 85 * 1080 / 720
x_end = 1160 * 1920 / 1280
y_end = 640 * 1080 / 720
screen = pygame.display.set_mode((0, 0))
X_SIZE = 105 * 10
Y_SIZE = 68 * 10

BOX_HEIGHT = (16.5 * 2 + 7.32) * 10 / Y_SIZE * (y_end - y_start)
BOX_WIDTH = 16.5 * 10 / X_SIZE * (x_end - x_start)

GOAL = 73.2 / Y_SIZE * (y_end - y_start)
GOAL_AREA_HEIGHT = (5.4864 * 20 + GOAL) * 1080 / 720
GOAL_AREA_WIDTH = (5.4864 * 10) * 1920 / 1280

SCALERS = np.array([1280 / 100, 720 / 100])

pencere = pygame.display.set_mode(boyut,pygame.SRCALPHA)


x = 0
y = 0


for i in range(5000,8000):
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen = pygame.display.set_mode(boyut)

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    screen.fill(WHITE)
    pygame.draw.rect(screen, (115, 130, 0), (x_start, y_start, x_end - x_start, y_end - y_start), 0)

    pencere.blit(screen, (0, 0))
    xtop = float(df[31][i]) * (x_end - x_start)
    ytop = float(1 - df[32][i]) * (y_end - y_start)
    x1 = float(df[3][i]) * (x_end - x_start)
    y1 = float(1 - df[4][i]) * (y_end - y_start)
    x2 = float(df[5][i]) * (x_end - x_start)
    y2 = float(1 - df[6][i]) * (y_end - y_start)
    x3 = float(df[7][i]) * (x_end - x_start)
    y3 = float(1 - df[8][i]) * (y_end - y_start)
    x4 = float(df[9][i]) * (x_end - x_start)
    y4 = float(1 - df[10][i]) * (y_end - y_start)
    x5 = float(df[11][i]) * (x_end - x_start)
    y5 = float(1 - df[12][i]) * (y_end - y_start)
    x6 = float(df[13][i]) * (x_end - x_start)
    y6 = float(1 - df[14][i]) * (y_end - y_start)
    x7 = float(df[15][i]) * (x_end - x_start)
    y7 = float(1 - df[16][i]) * (y_end - y_start)
    x8 = float(df[17][i]) * (x_end - x_start)
    y8 = float(1 - df[18][i]) * (y_end - y_start)
    x9 = float(df[19][i]) * (x_end - x_start)
    y9 = float(1 - df[20][i]) * (y_end - y_start)
    x10 = float(df[21][i]) * (x_end - x_start)
    y10 = float(1 - df[22][i]) * (y_end - y_start)
    x11 = float(df[23][i]) * (x_end - x_start)
    y11 = float(1 - df[24][i]) * (y_end - y_start)
    xt1 = float(df1[3][i]) * (x_end - x_start)
    yt1 = float(1 - df1[4][i]) * (y_end - y_start)
    xt2 = float(df1[5][i]) * (x_end - x_start)
    yt2 = float(1 - df1[6][i]) * (y_end - y_start)
    xt3 = float(df1[7][i]) * (x_end - x_start)
    yt3 = float(1 - df1[8][i]) * (y_end - y_start)
    xt4 = float(df1[9][i]) * (x_end - x_start)
    yt4 = float(1 - df1[10][i]) * (y_end - y_start)
    xt5 = float(df1[11][i]) * (x_end - x_start)
    yt5 = float(1 - df1[12][i]) * (y_end - y_start)
    xt6 = float(df1[13][i]) * (x_end - x_start)
    yt6 = float(1 - df1[14][i]) * (y_end - y_start)
    xt7 = float(df1[15][i]) * (x_end - x_start)
    yt7 = float(1 - df1[16][i]) * (y_end - y_start)
    xt8 = float(df1[17][i]) * (x_end - x_start)
    yt8 = float(1 - df1[18][i]) * (y_end - y_start)
    xt9 = float(df1[19][i]) * (x_end - x_start)
    yt9 = float(1 - df1[20][i]) * (y_end - y_start)
    xt10 = float(df1[21][i]) * (x_end - x_start)
    yt10 = float(1 - df1[22][i]) * (y_end - y_start)
    xt11 = float(df1[23][i]) * (x_end - x_start)
    yt11 = float(1 - df1[24][i]) * (y_end - y_start)

    if xtop == 0 or ytop == 0:
        xtop = 1930
        ytop = 1090

    points = ((-100, -100), (-100, 1580), (2520, -100), (2520, 1580), (x1 + x_start, y1 + y_start),
              (x2 + x_start, y2 + y_start), (x3 + x_start, y3 + y_start), (x4 + x_start, y4 + y_start),
              (x5 + x_start, y5 + y_start), (x6 + x_start, y6 + y_start), (x7 + x_start, y7 + y_start),
              (x8 + x_start, y8 + y_start), (x9 + x_start, y9 + y_start), (x10 + x_start, y10 + y_start),
              (x11 + x_start, y11 + y_start), (xt1 + x_start, yt1 + y_start), (xt2 + x_start, yt2 + y_start),
              (xt3 + x_start, yt3 + y_start), (xt4 + x_start, yt4 + y_start), (xt5 + x_start, yt5 + y_start),
              (xt6 + x_start, yt6 + y_start), (xt7 + x_start, yt7 + y_start), (xt8 + x_start, yt8 + y_start),
              (xt9 + x_start, yt9 + y_start), (xt10 + x_start, yt10 + y_start), (xt11 + x_start, yt11 + y_start))

    vor = spatial.Voronoi(points)
    ckk = vor.vertices
    ks = ckk.tolist()
    brr = ckk.tolist()
    del brr[-1]
    regions = vor.regions
    rst = vor.ridge_vertices
    region_point = vor.point_region.tolist()

    ct = 0
    for region in regions:

        if ct >= 0:
            srk = list()

            for j in region:

                if j == (-1):
                    srk = ()
                    break


                else:
                    srk.append(ks[j])

            poly = shapely.geometry.Polygon(srk)

            for knt in range(len(points)):
                P1 = shapely.geometry.Point(points[knt])

                if knt >= 4 and knt < 15:

                    if P1.within(poly) == True:
                        color = (0, 150, 150)
                else:

                    if P1.within(poly) == True:
                        color = (115, 100, 0)

            if len(srk) > 2:
                pygame.draw.polygon(screen, color, srk)

        ct = ct + 1
        if ct >= len(regions):
            break
    for ayi in rst:

        start = ks[ayi[0]]
        end = ks[ayi[1]]

        if (ayi[1] == (-1) or ayi[0] == (-1)):
            # pygame.draw.polygon(screen, WHITE, brr)
            pass

        else:
            pygame.draw.line(screen, WHITE, start, end, 3)
            # pass
        # Sahadışı
    pygame.draw.rect(screen, WHITE, (0, 0, x_start, 1080), 0)
    pygame.draw.rect(screen, WHITE, (x_start, y_end, 1920 - x_start, 1080 - y_end), 0)
    pygame.draw.rect(screen, WHITE, (x_start, 0, 1920 - x_start, y_start), 0)
    pygame.draw.rect(screen, WHITE, (x_end, y_start, 1920 - x_end, y_end), 0)

    # Saha kenar çizgileri

    pygame.draw.rect(screen, BLACK, (x_start, y_start, x_end - x_start, y_end - y_start), 3)

    # Yarı saha çizgisi
    pygame.draw.line(screen, BLACK, (x_start + (x_end - x_start) / 2, y_start),
                     (x_start + (x_end - x_start) / 2, y_end), 3)
    pygame.draw.circle(screen, BLACK, (int(x_start + (x_end - x_start) / 2), int(y_start + (y_end - y_start) / 2)),
                       int(91 * 1920 / 1280), 3)
    pygame.draw.circle(screen, BLACK, (int(x_start + (x_end - x_start) / 2), int(y_start + (y_end - y_start) / 2)), 3,
                       0)

    # Ceza Sahası çizgileri
    pygame.draw.rect(screen, BLACK, (x_start, y_start + (y_end - y_start - BOX_HEIGHT) / 2, BOX_WIDTH, BOX_HEIGHT), 3)
    pygame.draw.rect(screen, BLACK,
                     (x_end - BOX_WIDTH + 1, y_start + (y_end - y_start - BOX_HEIGHT) / 2, BOX_WIDTH, BOX_HEIGHT), 3)

    # Kaleler
    pygame.draw.rect(screen, BLACK, (x_start - 20, y_start + (y_end - y_start - GOAL) / 2, 21, GOAL), 3)
    pygame.draw.rect(screen, BLACK, (x_end - 1, y_start + (y_end - y_start - GOAL) / 2, 21, GOAL), 3)

    # Kale Sahası
    pygame.draw.rect(screen, BLACK,
                     (x_start, y_start + (y_end - y_start - GOAL_AREA_HEIGHT) / 2, GOAL_AREA_WIDTH, GOAL_AREA_HEIGHT),
                     3)
    pygame.draw.rect(screen, BLACK, (
        x_end - GOAL_AREA_WIDTH, y_start + (y_end - y_start - GOAL_AREA_HEIGHT) / 2, GOAL_AREA_WIDTH + 1,
        GOAL_AREA_HEIGHT),
                     3)

    # Penaltı Noktaları
    pygame.draw.circle(screen, BLACK, (int(x_start + (105 * 1920 / 1280)), int(y_start + (y_end - y_start) / 2)), 3, 0)
    pygame.draw.circle(screen, BLACK, (int(x_end - (105 * 1920 / 1280)), int(y_start + (y_end - y_start) / 2)), 3, 0)

    # Ceza yayları

    pygame.draw.arc(screen, BLACK, (
        x_start + (105 * 1920 / 1280) - (183 * 1920 / 1280) / 2, y_start + (y_end - y_start - (183 * 1920 / 1280)) / 2,
        (183 * 1920 / 1280), (183 * 1920 / 1280)), 2 * PI / 360 * 305, 2 * PI / 360 * 58, 3)
    pygame.draw.arc(screen, BLACK, (
        x_end - (105 * 1920 / 1280) - (183 * 1920 / 1280) / 2, y_start + (y_end - y_start - (183 * 1920 / 1280)) / 2,
        (183 * 1920 / 1280), (183 * 1920 / 1280)), 2 * PI / 360 * 122,
                    2 * PI / 360 * 240, 3)

    a = 10
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x1), int(y_start + y1)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x2), int(y_start + y2)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x3), int(y_start + y3)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x4), int(y_start + y4)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x5), int(y_start + y5)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x6), int(y_start + y6)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x7), int(y_start + y7)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x8), int(y_start + y8)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x9), int(y_start + y9)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x10), int(y_start + y10)), a)
    top = pygame.draw.circle(screen, (255, 0, 0), (int(x_start + x11), int(y_start + y11)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt1), int(y_start + yt1)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt2), int(y_start + yt2)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt3), int(y_start + yt3)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt4), int(y_start + yt4)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt5), int(y_start + yt5)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt6), int(y_start + yt6)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt7), int(y_start + yt7)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt8), int(y_start + yt8)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt9), int(y_start + yt9)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt10), int(y_start + yt10)), a)
    top = pygame.draw.circle(screen, (255, 255, 0), (int(x_start + xt11), int(y_start + yt11)), a)
    top = pygame.draw.circle(screen, (0, 0, 0), (int(x_start + xtop), int(y_start + ytop)), 5)
    pygame.display.update()

