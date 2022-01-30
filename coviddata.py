import json
import matplotlib.pyplot as plt
data_ubication="C://Users\carri\Documents\VSFolder\p5-and-processing\covidsimulator\data//at_5731.json"

with open(data_ubication) as f:
    data = json.load(f)
data=data["data"]

data_x=[i["time"] for i in data]
data_y_ill=[i["ill"] for i in data]
data_y_healthy=[i["healthy"] for i in data]
data_y_inmune=[i["inmune"] for i in data]
# data_y_dead=[i["dead"] for i in data]

# plt.stackplot(data_x, data_y_ill, data_y_healthy, data_y_inmune, data_y_dead, colors=["#c81230", "#161991", "#18af21", "#5c5a58"])
plt.stackplot(data_x, data_y_ill, data_y_healthy, data_y_inmune, colors=["#c81230", "#161991", "#18af21", "#5c5a58"])

plt.show()