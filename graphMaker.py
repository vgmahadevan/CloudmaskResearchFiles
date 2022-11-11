import os
import matplotlib.pyplot as plt

# Create graphs directory to deposit images

if not os.path.isdir("graphs"):
    os.makedirs("graphs")

for log in os.listdir():

    # Only consider the output logs, ignore the rest

    if "output" not in log:
        continue

    file = open(log, "r")

    dataLines = []

    for line in file:
        if "val_loss" in line:
            dataLines.append(line.rstrip())

    index = []
    loss = []
    accuracy = []
    val_loss = []
    val_accuracy = []

    # Put data from the end of each epoch into several lists

    for i in range(len(dataLines)):
        words = dataLines[i].split()
        index.append(i+1)
        for j in range(len(words)):
            if words[j] == "loss:":
                loss.append(float(words[j+1]))
            if words[j] == "accuracy:":
                accuracy.append(float(words[j+1]))
            if words[j] == "val_loss:":
                val_loss.append(float(words[j+1]))
            if words[j] == "val_accuracy:":
                val_accuracy.append(float(words[j+1]))

    # The following creates the plot for the graph for the training loss and accuracy

    fig, ax1 = plt.subplots()

    ax1.set_xlabel("Epochs")
    ax1.set_ylabel("Training Loss", color="red")
    ax1.plot(index, loss, color="red")
    ax1.tick_params(axis='y', labelcolor="red")

    ax2 = ax1.twinx()

    ax2.set_ylabel("Training Accuracy", color="blue")
    ax2.plot(index, accuracy, color="blue")
    ax2.tick_params(axis='y', labelcolor="blue")

    plt.title(log[7:-4]+" Training Loss and Accuracy")

    plt.savefig(os.path.join(os.path.curdir, "graphs", log[7:-4]+"_train.png"))
    
    # same as above but for validation set

    fig, ax1 = plt.subplots()

    ax1.set_xlabel("Epochs")
    ax1.set_ylabel("Validation Loss", color="red")
    ax1.plot(index, val_loss, color="red")
    ax1.tick_params(axis='y', labelcolor="red")

    ax2 = ax1.twinx()

    ax2.set_ylabel("Validation Accuracy", color="blue")
    ax2.plot(index, val_accuracy, color="blue")
    ax2.tick_params(axis='y', labelcolor="blue")

    plt.title(log[7:-4]+" Validation Loss and Accuracy")

    plt.savefig(os.path.join(os.path.curdir, "graphs", log[7:-4]+"_val.png"))

    plt.close()

