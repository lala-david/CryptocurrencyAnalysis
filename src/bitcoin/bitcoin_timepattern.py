import json
import matplotlib.pyplot as plt
import numpy as np

with open('./json/timepattern/output_1699986850.json', 'r') as f:
    data = json.load(f)

times = []
outputs = []
avg_outputs = []

for d in data:
    hour = int(d['datetime'][11:13])
    output = d['total_output']
    times.append(hour)
    outputs.append(output)

for i in range(24):
    vals = [o for t, o in zip(times, outputs) if t == i]
    if len(vals) == 0:
        avg = 0
    else:
        avg = sum(vals) / len(vals)
    avg_outputs.append(avg)
avg_times = np.arange(24)

plt.figure(figsize=(10, 4))
plt.plot(avg_times, avg_outputs, marker='o')
plt.scatter(times, outputs, s=5)
plt.xticks(avg_times)
plt.xlabel('Hour')
plt.ylabel('Average Output')
plt.title('Time Pattern')
plt.grid()
plt.savefig('./img/timepattern.png')

max_avg_output = max(avg_outputs)
max_avg_time = avg_times[np.argmax(avg_outputs)]
max_avg_time_str = f'{max_avg_time:02d}:00:00'

print(max_avg_output)
print(max_avg_time_str)