from src.pseudo_hilbert_curve import PseudoHilbertCurve
from src.hilbert_curve import HilbertCurve
from src.zhang_curve.zhang_curve import ZhangCurve
from src.metrics.perez_metric import perez_mean
from src.metrics.anns_metric import avg_anns
from src.metrics.spearman_metric import spearman_metric, cluster_spearman_metric
from src.snake_curve import SnakeCurve
from src.morton import MortonCurve
from src.curve_utils.dimension import Dimension
from src.metrics.metrics import metric_neighbor_from_curve, metric_neighbor_from_d
from src.curve_utils.plot_utils import plot_curve
from src.curve_utils.curve_validator import validate_curve

from matplotlib import pyplot as plt

# def main():
    # sizes = [(4, 4), (8, 8), (16, 16), (32, 32)]

    # for width, height in sizes:
    #     # ------------------ Generate Curves ------------------
    #     pseudo = PseudoHilbertCurve.from_dimension(Dimension(width, height))
    #     snake = SnakeCurve.from_dimension(Dimension(width, height))
    #     zhang = ZhangCurve.from_dimension(Dimension(width, height))
    #     morton = MortonCurve.from_dimension(Dimension(width, height))
    #     hilbert = HilbertCurve.from_dimension(Dimension(width, height))

    #     # ------------------ Generate Plots ------------------

    #     plot_pseudo = plot_curve(pseudo)

    #     ax = plt.subplot()
    #     ax.add_collection(plot_pseudo)

    #     plt.savefig(f"./plots/pseudo_{width}x{height}.png")
    #     ax.cla()

    #     plot_snake = plot_curve(snake)

    #     ax = plt.subplot()
    #     ax.add_collection(plot_snake)

    #     plt.savefig(f"./plots/snake_{width}x{height}.png")
    #     ax.cla()

    #     plot_zhang = plot_curve(zhang)

    #     ax = plt.subplot()
    #     ax.add_collection(plot_zhang)

    #     plt.savefig(f"./plots/zhang_{width}x{height}.png")
    #     ax.cla()

    #     plot_morton = plot_curve(morton)

    #     ax = plt.subplot()
    #     ax.add_collection(plot_morton)

    #     plt.savefig(f"./plots/morton_{width}x{height}.png")
    #     ax.cla()

    #     plot_hilbert = plot_curve(hilbert)

    #     ax = plt.subplot()
    #     ax.add_collection(plot_hilbert)

    #     plt.savefig(f"./plots/hilbert_{width}x{height}.png")
    #     ax.cla()


    #     # ------------------ Generate Metrics ------------------
    #     anns_pseudo = avg_anns(pseudo)
    #     anns_snake = avg_anns(snake)
    #     anns_zhang = avg_anns(zhang)
    #     anns_morton = avg_anns(morton)
    #     anns_hilbert = avg_anns(hilbert)

    #     perez_pseudo = perez_mean(pseudo)
    #     perez_snake = perez_mean(snake)
    #     perez_zhang = perez_mean(zhang)
    #     perez_morton = perez_mean(morton)
    #     perez_hilbert = perez_mean(hilbert)

    #     spearman_pseudo = cluster_spearman_metric(pseudo)
    #     spearman_snake = cluster_spearman_metric(snake)
    #     spearman_zhang = cluster_spearman_metric(zhang)
    #     spearman_morton = cluster_spearman_metric(morton)
    #     spearman_hilbert = cluster_spearman_metric(hilbert)

    #     metric_1_pseudo = metric_1(pseudo)
    #     metric_1_snake = metric_1(snake)
    #     metric_1_zhang = metric_1(zhang)
    #     metric_1_morton = metric_1(morton)
    #     metric_1_hilbert = metric_1(hilbert)

    #     metric_2_pseudo = metric_2(pseudo)
    #     metric_2_snake = metric_2(snake)
    #     metric_2_zhang = metric_2(zhang)
    #     metric_2_morton = metric_2(morton)
    #     metric_2_hilbert = metric_2(hilbert)

    #     # ------------------ Write Metrics ------------------
    #     with open("./results/metrics.txt", "a") as f:
    #         f.write(f"Width: {width}, Height: {height}\n")
    #         f.write(f"Curve: Pseudo, Snake, Zhang, Morton, Hilbert\n")
    #         f.write(f"ANNs: {anns_pseudo}, {anns_snake}, {anns_zhang}, {anns_morton}, {anns_hilbert}\n")
    #         f.write(f"Perez: {perez_pseudo}, {perez_snake}, {perez_zhang}, {perez_morton}, {perez_hilbert}\n")
    #         f.write(f"Spearman: {spearman_pseudo}, {spearman_snake}, {spearman_zhang}, {spearman_morton}, {spearman_hilbert}\n")
    #         f.write(f"Metric 1: {metric_1_pseudo}, {metric_1_snake}, {metric_1_zhang}, {metric_1_morton}, {metric_1_hilbert}\n")
    #         f.write(f"Metric 2: {metric_2_pseudo}, {metric_2_snake}, {metric_2_zhang}, {metric_2_morton}, {metric_2_hilbert}\n")
    #         f.write("\n")

    # width, height = 6, 4
    # zhang = ZhangCurve.from_dimension(Dimension(width, height))
    # plot_zhang = plot_curve(zhang)
    
    # fig, ax = plt.subplots()
    # ax.add_collection(plot_zhang)
    # plt.savefig(f"./plots/zhang_{width}x{height}.png")
    
# if __name__ == "__main__":
#     main()




# x = 30
# y = 30

# curve1 = PseudoHilbertCurve.from_dimension(Dimension(x, y))
# curve2 = SnakeCurve.from_dimension(Dimension(x, y))
# curve3 = ZhangCurve.from_dimension(Dimension(x, y))
# curve4 = MortonCurve.from_dimension(Dimension(x, y))

# perez_pseudo_hilbert = perez_mean(curve1)
# perez_snake = perez_mean(curve2)
# perez_zhang = perez_mean(curve3)
# perez_morton = perez_mean(curve4)

# anns_pseudo_hilbert = avg_anns(curve1)
# anns_snake = avg_anns(curve2)
# anns_zhang = avg_anns(curve3)
# anns_morton = avg_anns(curve4)

# spearman_pseudo_hilbert = cluster_spearman_metric(curve1)
# spearman_snake = cluster_spearman_metric(curve2)
# spearman_zhang = cluster_spearman_metric(curve3)
# spearman_morton = cluster_spearman_metric(curve4)

# pseudo_hilbert_metric_1 = metric_1(curve1)
# snake_metric_1 = metric_1(curve2)
# zhang_metric_1 = metric_1(curve3)
# morton_metric_1 = metric_1(curve4)


# pseudo_hilbert_metric_2 = metric_2(curve1)
# snake_metric_2 = metric_2(curve2)
# zhang_metric_2 = metric_2(curve3)
# morton_metric_2 = metric_2(curve4)

# fig, ax = plt.subplots(2, 3, figsize=(10, 6))
# ax.flatten()
# # plot metrics with barplot
# ax[0, 0].bar(["Pseudo Hilbert", "Snake", "Zhang"], [perez_pseudo_hilbert, perez_snake, perez_zhang])
# ax[0, 0].set_title("Perez Mean")
# ax[0, 1].bar(["Pseudo Hilbert", "Snake", "Zhang"], [anns_pseudo_hilbert, anns_snake, anns_zhang])
# ax[0, 1].set_title("Average Nearest Neighbor Stretch")
# ax[1, 0].bar(["Pseudo Hilbert", "Snake", "Zhang"], [spearman_pseudo_hilbert, spearman_snake, spearman_zhang])
# ax[1, 0].set_title("Spearman Metric")
# ax[1, 1].bar(["Pseudo Hilbert", "Snake", "Zhang"], [pseudo_hilbert_metric_1, snake_metric_1, zhang_metric_1])
# ax[1, 1].set_title("Metric 1")
# ax[0, 2].bar(["Pseudo Hilbert", "Snake", "Zhang"], [pseudo_hilbert_metric_2, snake_metric_2, zhang_metric_2])
# ax[0, 2].set_title("Metric 2")

# plot curves
# fig, ax = plt.subplots()
# ax.add_collection(plot_curve(curve1))
# ax.add_collection(plot_curve(curve2))
# ax.add_collection(plot_curve(curve3))
# plot_curve(curve4, "Morton Curve")

# plt.tight_layout()
# plt.show()


# print("Perez Mean")
# print("--------------------------------")
# print("Pseudo Hilbert:", perez_pseudo_hilbert)
# print("Snake: ", perez_snake)
# print("Zhang: ", perez_zhang)


# print("Morton: ", perez_morton)
# print()
# print("Average Nearest Neighbor Stretch")
# print("--------------------------------")
# print("Pseudo Hilbert:", anns_pseudo_hilbert)
# print("Snake: ", anns_snake)
# print("Zhang: ", anns_zhang)
# print("Morton: ", anns_morton)
# print()
# print("Spearman Metric")
# print("--------------------------------")
# print("Pseudo Hilbert:", spearman_pseudo_hilbert)
# print("Snake: ", spearman_snake)
# print("Zhang: ", spearman_zhang)
# print("Morton: ", spearman_morton)
# print()
# print("Metric 1")
# print("--------------------------------")
# print("Pseudo Hilbert:", pseudo_hilbert_metric_1)
# print("Snake: ", snake_metric_1)
# print("Zhang: ", zhang_metric_1)
# print("Morton: ", morton_metric_1)
# print()
# print("Metric 2")
# print("--------------------------------")
# print("Pseudo Hilbert:", pseudo_hilbert_metric_2)
# print("Snake: ", snake_metric_2)
# print("Zhang: ", zhang_metric_2)
# print("Morton: ", morton_metric_2)
# print()

height = 8
width = 8
# curve = ZhangCurve(width*height, Dimension(width, height))
# curve = PseudoHilbertCurve(width*height, Dimension(width, height), 3, True)
# curve = SnakeCurve(width*height, Dimension(width, height))
curve = MortonCurve(width*height, Dimension(width, height))

fig, ax = plt.subplots(figsize=(10, 10))
ax.add_collection(plot_curve(curve))
plt.show()


# for i in range(90, 100):
#     for j in range(90, 100):
#         curve = PseudoHilbertCurve(i*j, Dimension(i, j), 3, True)
#         result = validate_curve(curve)
#         print(f"Width: {i}, Height: {j}")
#         print(result)
#         print()


# w = 4
# h = 4
# curve1 = HilbertCurve(w*h, Dimension(w, h))
# curve2 = MortonCurve(w*h, Dimension(w, h))
# curve3 = SnakeCurve(w*h, Dimension(w, h))
# curve4 = ZhangCurve(w*h, Dimension(w, h))
# curve5 = PseudoHilbertCurve(w*h, Dimension(w, h), 3, True)

# print("Perez Mean")
# print(perez_mean(curve1))
# print(perez_mean(curve2))
# print(perez_mean(curve3))
# print(perez_mean(curve4))
# print(perez_mean(curve5))
# print()


# w = 8
# h = 8
# curve1 = HilbertCurve(w*h, Dimension(w, h))
# curve2 = MortonCurve(w*h, Dimension(w, h))
# curve3 = SnakeCurve(w*h, Dimension(w, h))
# curve4 = ZhangCurve(w*h, Dimension(w, h))
# curve5 = PseudoHilbertCurve(w*h, Dimension(w, h), 3, True)

# print("Perez Mean")
# print("%.3f" % perez_mean(curve1), file=open("results.txt", "a"))
# print("%.3f" % perez_mean(curve2), file=open("results.txt", "a"))
# print("%.3f" % perez_mean(curve3), file=open("results.txt", "a"))
# print("%.3f" % perez_mean(curve4), file=open("results.txt", "a"))
# print("%.3f" % perez_mean(curve5), file=open("results.txt", "a"))
# print()

# w = 50
# h = 50
# curve1 = HilbertCurve(w*h, Dimension(w, h))
# curve2 = MortonCurve(w*h, Dimension(w, h))
# curve3 = SnakeCurve(w*h, Dimension(w, h))
# curve4 = ZhangCurve(w*h, Dimension(w, h))
# curve5 = PseudoHilbertCurve(w*h, Dimension(w, h), 0, True)

# print("Perez Mean")
# print("%.3f" % perez_mean(curve1), file=open("results.txt", "a"))
# print("%.3f" % perez_mean(curve2), file=open("results.txt", "a"))
# print("%.3f" % perez_mean(curve3), file=open("results.txt", "a"))
# print("%.3f" % perez_mean(curve4), file=open("results.txt", "a"))
# print("KSC: %.3f" % perez_mean(curve5), file=open("results.txt", "a"))
# print()

# widths = [4, 8, 16, 32, 4, 5, 6, 8, 4, 10, 10, 4, 12, 8, 15, 50]
# heights = [4, 8, 16, 32, 5, 4, 6, 4, 8, 10, 4, 10, 8, 12, 15, 50]

# with open("results.txt", "w") as file:
#     file.write(f"Perez Metric\n")


# for w, h in zip(widths, heights):
#     curve1 = None
#     curve2 = None
#     try:
#         curve1 = HilbertCurve(w*h, Dimension(w, h))
#         curve2 = MortonCurve(w*h, Dimension(w, h))
#     except:
#         pass
#     curve3 = SnakeCurve(w*h, Dimension(w, h))
#     curve4 = ZhangCurve(w*h, Dimension(w, h))
#     curve5 = PseudoHilbertCurve(w*h, Dimension(w, h), 0, True)

#     with open("results.txt", "a") as file:
#         file.write(f"Width: {w}, Height: {h}\n")
        
#     if curve1 is not None and curve2 is not None:
#         print("Hilbert: %.0f" % metric_neighbor_from_curve(curve1), file=open("results.txt", "a"))
#         print("Morton: %.0f" % metric_neighbor_from_curve(curve2), file=open("results.txt", "a"))
#     else:
#         print("Hilbert: x", file=open("results.txt", "a"))
#         print("Morton: x", file=open("results.txt", "a"))
#     print("Snake: %.0f" % metric_neighbor_from_curve(curve3), file=open("results.txt", "a"))
#     print("Zhnag: %.0f" % metric_neighbor_from_curve(curve4), file=open("results.txt", "a"))
#     print("KSC: %.0f" % metric_neighbor_from_curve(curve5), file=open("results.txt", "a"))
#     print(file=open("results.txt", "a"))

# w = 4
# h = 10
# curve1 = HilbertCurve(w*h, Dimension(w, h))
# curve2 = MortonCurve(w*h, Dimension(w, h))
# curve3 = SnakeCurve(w*h, Dimension(w, h))
# curve4 = ZhangCurve(w*h, Dimension(w, h))
# curve5 = PseudoHilbertCurve(w*h, Dimension(w, h), 3, True)

# with open("results.txt", "w") as file:
#     file.write(f"Width: {w}, Height: {h}\n")
# print("avg_anns")
# print("%.3f" % avg_anns(curve1), file=open("results.txt", "a"))
# print("%.3f" % avg_anns(curve2), file=open("results.txt", "a"))
# print("%.3f" % avg_anns(curve3), file=open("results.txt", "a"))
# print("%.3f" % avg_anns(curve4), file=open("results.txt", "a"))
# print("%.3f" % avg_anns(curve5), file=open("results.txt", "a"))
# print()