from misc_sim_funcs import *
from network import *
from constants import  *


initialize_output_files()

#create/init network
net = Network()
net.fill_network(V + NoOfSources + NoOfDataCenters)
net.load_primary_users()

#Open LLC_path.txt, LLC_spectrum.txt, generated_messages, specBW, LINK_EXISTS
path_lines, spec_lines, msg_lines, specBW, LINK_EXISTS = get_data_structs()

q_tables_path = "Q_tables"

# for loading the q tables
# q_tables_file = open(q_tables_path + "/q_tables.txt", "r")
# lines = q_tables_file.readlines()
# i = 0
# for node in net.nodes:
#     node.q_table = lines[i].strip().split(" ")
#     node.q_table = list(map(float, node.q_table))
#     i = i + 1
#
# q_tables_file.close()
#loop thru each tau
for node in net.nodes:
    node.q_table = np.array(node.q_table)
for t in range(0, T, tau):
    # print("TIME:", t)
    # net.network_status()
    # does all routing and sending of packets in the tau = t
    net.network_GO(t, specBW, path_lines, spec_lines, msg_lines, LINK_EXISTS)

# For saving the q tables

# if not os.path.exists(q_tables_path):
#     os.makedirs(q_tables_path)
# q_tables_file = open(q_tables_path + "/q_tables.txt", "w")
# for node in net.nodes:
#     for q_values in node.q_table:
#         q_tables_file.write(str(q_values) + " ")
#     q_tables_file.write("\n")
# q_tables_file.close()
#creates not_delivered.txt for overhead computation
net.not_delivered_messages()

# Handle messages that got delivered
net.messages_delivered()

# print average queue length at each node
average_queue_length = []
for node in net.nodes:
    avg_queue = sum(node.buf_length) / len(node.buf_length)
    average_queue_length.append(avg_queue)
    # print(node.buf_length[420])
    # print(node.count)
print(average_queue_length)

# saves packets per tau and parallel communications
net.save_packets_per_tau()
# net.print_bandusage()



