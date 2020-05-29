from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import os

path = "DataMules/Lexington/50/1/Link_Exists/"
num_Pusers = [0, 25, 50, 75, 100, 125, 150]
Xchant_mdr = []
Xchant_latency = []

for pusers in num_Pusers:
    path_to_metrics = path + "LE_" + str(1) + "_" + str(480) + "/" + "XChant_ALL/mules_" + \
                          str(24) + "/channels_" + str(6) + "/P_users_" + str(pusers) + \
                           "/msgfile_" + str(1) + "_" + str(15) + "/puserfile_" \
                           + str(0) + "/TTL_" + str(60) + "/BuffSize_" + str(-1) +"/" + "numTransceivers_"\
                            + str(1) + "/" + "/metrics.txt"

    with open(path_to_metrics, "r") as f:
        lines = f.readlines()[1:]
    line = lines[-1].strip().split()
    Xchant_mdr.append(float(line[1]))
    Xchant_latency.append(float(line[2]))

Xchant_mdr_LTE = [1, 0.82, 0.51,0.47,0.47,0.47,0.47]
Xchant_latency_LTE = [3.02, 8.21,4.05,1.32,1.32,1.32,1.32]
Xchant_latency_TV = [3.02, 4.3, 6.75, 3.1, 3.1, 2.72, 2.72]
Xchant_mdr_TV = [1.0, 1.0, 0.61, 0.56, 0.56, 0.56, 0.56]

q_learning_mdr_ALL = [0.896,  0.9715, 0.968,  0.9565, 0.9795, 0.973,  0.9675]
q_learning_mdr_TV= [0.896,  0.9715, 0.968,  0.9565, 0.9795, 0.973,  0.9675]
# q_learning_mdr_ISM =[0.,,,0.,,,0.,,,0.,,,0.,,,0.,,,0.,,]
q_learning_mdr_LTE = [0.902,  0.8635, 0.89,   0.8875, 0.8845, 0.8825, 0.8895]
q_learning_mdr_CBRS = [0.29,0.29,0.29,0.29,0.28,0.29,0.29]

q_learning_latency_ALL = [17.467,  13.292,  12.464,  12.913,  12.3245, 12.435,  12.356]
q_learning_latency_TV = [17.467,  13.292,  12.464,  12.913,  12.3245, 12.435,  12.356]
# q_learning_latency_ISM,=,,[,0.,,,,0.,,,,0.,,,,0.,,,,0.,,,,0.,,,,0.,,]
q_learning_latency_LTE = [17.113,  18.7345, 19.0575, 18.239,  18.78,   18.319,  19.007]
q_learning_latency_CBRS = [6.32,5.84,7.33,7.64,6.77,10.29,9.87]

fig = plt.figure()
ax = plt.subplot(111)

plt.xticks(np.arange(0, 160, step=25), fontsize=15)
plt.yticks(fontsize=15)
# plt.ylabel('Message delivery ratio', fontsize=15)
plt.ylabel('Latency(seconds)', fontsize = 15)
plt.xlabel('Number of primary users', fontsize=15)

# ax.plot(num_Pusers, Xchant_mdr_TV, '-', num_Pusers, q_learning_mdr_TV, '-', num_Pusers, Xchant_mdr_LTE, '--', num_Pusers, q_learning_mdr_LTE, '--')
ax.plot(num_Pusers, Xchant_latency_TV, '-', num_Pusers, q_learning_latency_TV, '-', num_Pusers, Xchant_latency_LTE, '--', num_Pusers, q_learning_latency_LTE, '--')
# ax.plot(num_Pusers, Xchant_latency, num_Pusers, q_learning_latency_ALL)
valid_markers = ([item[0] for item in matplotlib.markers.MarkerStyle.markers.items() if
item[1] is not 'nothing' and not item[1].startswith('tick') and not item[1].startswith('caret')])
markers = np.random.choice(valid_markers, 4, replace=False)
# box = ax.get_position()
# ax.set_position([box.x0, box.y0 + box.height * 0,
#                  box.width, box.height * 1])
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])

ax.legend(["dDSAaR (PU-TV)", "BARD (PU-TV)", "dDSAaR (PU-LTE)", "BARD (PU-LTE)", "BARD (TV)"], loc = "center", bbox_to_anchor=(0.8, 0.4), fontsize=12, ncol = 1)
# plt.tight_layout()
plot_path = "Plots"

if not os.path.exists(plot_path):
    os.makedirs(plot_path)
fig_name = "Plots/Spec_case_Latency_num_primary_users_Tv_LTE.eps"
# fig_name = "Plots/Spec_case_Latency_num_primary_users_TV.eps"
plt.savefig(fig_name)

plt.show()


print(Xchant_latency)
print(Xchant_mdr)