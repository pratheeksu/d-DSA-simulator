from matplotlib import pyplot as plt
import numpy as np

path = "DataMules/Lexington/50/1/Link_Exists/"
num_Pusers = [0, 25, 50, 75, 100, 125, 150]
bands = ["ALL", "TV", "ISM", "LTE", "CBRS"]
t = np.arange(0, 500, 30)
# q_learning_mdr = np.zeros((len(bands), len(num_Pusers)))
q_learning_mdr = np.zeros((len(bands), len(t)))
# q_learning_latency = np.zeros((len(bands), len(num_Pusers)))
q_learning_latency = np.zeros((len(bands), len(t)))
j = 0
for band in ["ALL"]:
    i = 0
    for pusers in num_Pusers:
        avg_mdr = 0
        avg_latency = 0
        for round in range(20):

            path_to_metrics = path + "LE_" + str(1) + "_" + str(480) + "/" + "q_learning_" + band + "/" + str(round) +\
                              "/mules_" + str(24) + "/channels_" + str(6) + "/P_users_" + str(pusers) + \
                                   "/msgfile_" + str(1) + "_" + str(15) + "/puserfile_" \
                                   + str(0) + "/TTL_" + str(60) + "/BuffSize_" + str(-1) +"/" + "numTransceivers_"\
                                    + str(1) + "/" + "/metrics.txt"

            with open(path_to_metrics, "r") as f:
                lines = f.readlines()[1:]
            # for line in lines:
            line_arr = lines[-1].strip().split()
            avg_mdr += float(line_arr[1])
            avg_latency += float(line_arr[2])
        q_learning_mdr[j, i] = avg_mdr / 20
        q_learning_latency[j, i] = avg_latency / 20
        i = i + 1
    j = j + 1

print(q_learning_mdr)
print(q_learning_latency)