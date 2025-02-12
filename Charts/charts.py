import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for plots
sns.set_style("whitegrid")

# 1. Model Accuracy
categories = ['Joy', 'Sadness', 'Anger', 'Neutral']
accuracy_scores = [92.5, 91.8, 92.3, 92.0]  # Accuracy, Precision, Recall, F1-Score

plt.figure(figsize=(8, 5))
sns.barplot(x=categories, y=accuracy_scores, palette="viridis")
plt.title("Model Accuracy and Performance Metrics")
plt.ylabel("Percentage (%)")
plt.ylim(90, 95)
for i, score in enumerate(accuracy_scores):
    plt.text(i, score + 0.2, f"{score}%", ha='center')
plt.show()

# 2. Low Latency
latency_data = [180, 200, 190, 185, 175]  # Latency in milliseconds for 5 test runs
time_points = np.arange(1, 6)

plt.figure(figsize=(8, 5))
plt.plot(time_points, latency_data, marker='o', linestyle='-', color='blue')
plt.title("Latency Performance Over Test Runs")
plt.xlabel("Test Run")
plt.ylabel("Latency (ms)")
plt.ylim(170, 210)
for i, latency in enumerate(latency_data):
    plt.text(time_points[i], latency + 5, f"{latency}ms", ha='center')
plt.show()

# 3. Scalability and Throughput
throughput_data = [1000, 1100, 1200, 1150, 1050]  # Events per second for 5 stress tests
load_levels = ['Low', 'Medium', 'High', 'Very High', 'Peak']

plt.figure(figsize=(8, 5))
sns.barplot(x=load_levels, y=throughput_data, palette="magma")
plt.title("System Throughput Under Different Loads")
plt.xlabel("Load Level")
plt.ylabel("Events per Second")
plt.ylim(900, 1300)
for i, throughput in enumerate(throughput_data):
    plt.text(i, throughput + 20, f"{throughput}/s", ha='center')
plt.show()

# 4. Streamlined Data Pipeline
data_loss = [0.05, 0.04, 0.06, 0.05, 0.03]  # Data loss percentage for 5 test runs
processing_delay = [0.8, 0.9, 0.7, 0.85, 0.75]  # Processing delay in seconds

plt.figure(figsize=(8, 5))
plt.plot(time_points, data_loss, marker='o', linestyle='-', color='red', label='Data Loss (%)')
plt.plot(time_points, processing_delay, marker='o', linestyle='-', color='green', label='Processing Delay (s)')
plt.title("Data Pipeline Efficiency Over Test Runs")
plt.xlabel("Test Run")
plt.ylabel("Percentage / Seconds")
plt.legend()
plt.ylim(0, 1)
for i, (loss, delay) in enumerate(zip(data_loss, processing_delay)):
    plt.text(time_points[i], loss + 0.05, f"{loss}%", ha='center')
    plt.text(time_points[i], delay + 0.05, f"{delay}s", ha='center')
plt.show()

# 5. Resource Utilization
resources = ['CPU', 'RAM', 'Storage']
usage = [65, 13, 55]  # CPU (%), RAM (GB), Storage (GB)

plt.figure(figsize=(8, 5))
sns.barplot(x=resources, y=usage, palette="plasma")
plt.title("Resource Utilization")
plt.ylabel("Usage (%) / (GB)")
plt.ylim(0, 100)
for i, value in enumerate(usage):
    plt.text(i, value + 2, f"{value}{'%' if i == 0 else 'GB'}", ha='center')
plt.show()

# 6. Ethical Standards
privacy_metrics = ['Data Anonymization', 'API Authentication', 'Transparent Monitoring']
scores = [100, 100, 100]  # All metrics achieved 100% compliance

plt.figure(figsize=(8, 5))
sns.barplot(x=privacy_metrics, y=scores, palette="coolwarm")
plt.title("Ethical Standards Compliance")
plt.ylabel("Percentage (%)")
plt.ylim(90, 110)
for i, score in enumerate(scores):
    plt.text(i, score + 2, f"{score}%", ha='center')
plt.show()