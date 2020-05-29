from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import os

path = "DataMules/Lexington/50/1/Link_Exists/"
num_Pusers = [0, 25, 50, 75, 100, 125, 150]
Xchant_mdr = []
Xchant_latency = []

for pusers in num_Pusers:
    path_to_metrics = path + "LE_" + str(1) + "_" + str(480) + "/" + "XChant_LTE/mules_" + \
                          str(24) + "/channels_" + str(6) + "/P_users_" + str(pusers) + \
                           "/msgfile_" + str(1) + "_" + str(15) + "/puserfile_" \
                           + str(0) + "/TTL_" + str(60) + "/BuffSize_" + str(-1) +"/" + "numTransceivers_"\
                            + str(1) + "/" + "/metrics.txt"

    with open(path_to_metrics, "r") as f:
        lines = f.readlines()[1:]
    print(len(lines))
    line = lines[-1].strip().split()
    Xchant_mdr.append(float(line[1]))
    Xchant_latency.append(float(line[2]))

q_learning_mdr_ALL = [0.903, 0.945,  0.9545, 0.901,  0.8455, 0.6305, 0.382]
q_learning_mdr_TV= [0.675,  0.434,  0.172,  0.0775, 0.0195, 0.0035, 0.0015]
# q_learning_mdr_ISM =[0.,,,0.,,,0.,,,0.,,,0.,,,0.,,,0.,,]
q_learning_mdr_LTE = [0.9355, 0.9205, 0.839,  0.656,  0.612, 0.452, 0.24]
q_learning_mdr_CBRS = [0.29,0.29,0.29,0.29,0.28,0.29,0.29]

q_learning_latency_ALL = [17.0575, 16.107, 14.028, 16.6665, 16.4025, 20.02, 18.515]
q_learning_latency_TV = [17.539,  21.9775, 38.888,  50.151,  48.804,  44.3,    41.975]
# q_learning_latency_ISM,=,,[,0.,,,,0.,,,,0.,,,,0.,,,,0.,,,,0.,,,,0.,,]
q_learning_latency_LTE = [14.341,  15.262,  16.111,  16.473,  16.0235, 18.806,  21.275]
q_learning_latency_CBRS = [ 6.7665,  6.6385,  6.524,  6.452,   6.8215,  9.0695, 11.485 ]

fig = plt.figure()
ax = plt.subplot(111)

plt.xticks(np.arange(0, 160, step=25), fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Message delivery ratio', fontsize=15)
# plt.ylabel(' Latency (seconds)', fontsize = 15)
plt.xlabel('Number of primary users', fontsize=15)

ax.plot(num_Pusers, Xchant_mdr, num_Pusers, q_learning_mdr_ALL, num_Pusers, q_learning_mdr_CBRS, num_Pusers,  q_learning_mdr_LTE, num_Pusers, q_learning_mdr_TV)
# ax.plot(num_Pusers, Xchant_latency, num_Pusers, q_learning_latency_ALL, num_Pusers, q_learning_latency_CBRS, num_Pusers,  q_learning_latency_LTE, num_Pusers, q_learning_latency_TV)
valid_markers = ([item[0] for item in matplotlib.markers.MarkerStyle.markers.items() if
item[1] is not 'nothing' and not item[1].startswith('tick') and not item[1].startswith('caret')])
markers = np.random.choice(valid_markers, 6, replace=False)
# box = ax.get_position()
# ax.set_position([box.x0, box.y0 + box.height * 0,
#                  box.width, box.height * 1])
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])

ax.legend(["dDSAaR", "BARD (ALL)", "BARD (CBRS)", "BARD (LTE)", "BARD (TV)"], loc = "best", fontsize=8, ncol = 2)
# plt.tight_layout()
plot_path = "Plots"

if not os.path.exists(plot_path):
    os.makedirs(plot_path)
fig_name = "Plots/MDR_num_primary_users.eps"
# fig_name = "Plots/Latency_num_primary_users.eps"
plt.savefig(fig_name)

plt.show()


print(Xchant_latency)
print(Xchant_mdr)