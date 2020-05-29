from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import os

path = "DataMules/Lexington/50/1/Link_Exists/"
num_Pusers = [0, 25, 50, 75, 100, 125, 150]
t = np.arange(30, 500, 30)

Xchant_mdr = []
Xchant_latency = []

for pusers in [100]:
    path_to_metrics = path + "LE_" + str(1) + "_" + str(480) + "/" + "XChant_LTE/mules_" + \
                          str(24) + "/channels_" + str(6) + "/P_users_" + str(pusers) + \
                           "/msgfile_" + str(1) + "_" + str(15) + "/puserfile_" \
                           + str(0) + "/TTL_" + str(60) + "/BuffSize_" + str(-1) +"/" + "numTransceivers_"\
                            + str(1) + "/" + "/metrics.txt"

    with open(path_to_metrics, "r") as f:
        lines = f.readlines()[2:]
    for line in lines:
        line_arr = line.strip().split()
        # print(line_arr)
        Xchant_mdr.append(float(line_arr[1]))
        Xchant_latency.append(float(line_arr[2]))

q_learning_mdr_ALL = [0.18, 0.29, 0.49, 0.57, 0.66, 0.72, 0.72, 0.75, 0.77, 0.79, 0.8,  0.81, 0.82,
  0.85, 0.87, 0.87]
q_learning_mdr_TV = [0, 0.04, 0.03, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
  0.02, 0.02, 0.02]
#,q_learning_mdr_ISM,=[0.,,,0.,,,0.,,,0.,,,0.,,,0.,,,0.,,]
q_learning_mdr_LTE =[0, 0.17, 0.18, 0.31, 0.41, 0.47, 0.5,  0.52, 0.55, 0.56, 0.59, 0.57, 0.56,
  0.58, 0.62, 0.62]
q_learning_mdr_CBRS = [0, 0.12, 0.15, 0.22, 0.25, 0.26, 0.27, 0.27, 0.29, 0.29, 0.29, 0.27, 0.28,
  0.29, 0.29, 0.29]

q_learning_latency_ALL = [12.5,  26.86, 25.58, 20.77, 20.34, 20.41, 19.79, 19.58, 18.34, 17.56, 16.79,
  16.81, 16.86, 17.35, 17.48, 17.48]
q_learning_latency_TV = [0,0,0,18,28.33,29.57,36.46,39,39,41.33,42.95,42.95,43.71,44.93,45.29,45.72]
#,q_learning_latency_ISM,=,,[,0.,,,,0.,,,,0.,,,,0.,,,,0.,,,,0.,,,,0.,,]
q_learning_latency_LTE = [ 0,   36.25, 25.57, 11.48,  9.77, 10.72, 10.53, 11.85, 11.95, 13.5,  13.08,
  12.57, 12.36, 12.41, 13.97, 13.97]
q_learning_latency_CBRS = [ 0, 28.67, 22.5,  13.2,  12.14, 11.08, 10.03,  9.11,  8.52,  7.69,  7.36,
   6.95,  6.82,  6.7,   6.7,   6.7 ]

fig = plt.figure()
ax = plt.subplot(111)

plt.xticks(np.arange(0, 490, step=60), fontsize=15)
plt.yticks(fontsize=15)
# plt.ylabel('Message delivery ratio', fontsize=15)
plt.ylabel('Latency (seconds)', fontsize = 15)
plt.xlabel('Simulation time (seconds)', fontsize=15)
# plt.ylim(0, 1)

# ax.plot(t, Xchant_mdr, t, q_learning_mdr_ALL, t, q_learning_mdr_CBRS, t,  q_learning_mdr_LTE, t, q_learning_mdr_TV)
ax.plot(t, Xchant_latency, t, q_learning_latency_ALL, t, q_learning_latency_CBRS, t,  q_learning_latency_LTE, t, q_learning_latency_TV)
valid_markers = ([item[0] for item in matplotlib.markers.MarkerStyle.markers.items() if
item[1] is not 'nothing' and not item[1].startswith('tick') and not item[1].startswith('caret')])
markers = np.random.choice(valid_markers, 6, replace=False)
# box = ax.get_position()
# ax.set_position([box.x0, box.y0 + box.height * 0,
#                  box.width, box.height * 1])
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])

ax.legend(["dDSAaR", "BARD (ALL)", "BARD (CBRS)", "BARD (LTE)", "BARD (TV)"], loc = "best", fontsize=8, ncol = 3)
# plt.tight_layout()
plot_path = "Plots"

if not os.path.exists(plot_path):
    os.makedirs(plot_path)
# fig_name = "Plots/MDR_simulation_time.eps"
fig_name = "Plots/Latency_simulation_time.eps"

plt.savefig(fig_name)

plt.show()


print(Xchant_latency)
print(Xchant_mdr)