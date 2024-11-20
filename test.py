import json

file = open('data.json', 'r')
data = json.load(file)

classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck']

targets = []
img_id = []
for key in data.keys():
    parts = key.split('_')
    label = '_'.join(parts[1:])[:-4]
    img_id.append(key[:-4])
    targets.append(classes.index(label))

def calculate_scores(data):
    scores = []
    for i in range(10):
        patch_score = 0
        for j in range(len(data[i])):
            if sum(data[i][j]) > patch_score:
                patch_score = sum(data[i][j])
        scores.append(patch_score)
    return scores, scores.index(max(scores))

def calculate_scores(data):
    scores = []
    for i in range(10):
        scores.append(sum(sum(row) for row in data[i]))
    return scores, scores.index(max(scores))

correct = 0
total = 0
for key in data.keys():
    total += 1
    scores, pred = calculate_scores(data[key])
    if pred == targets[img_id.index(key[:-4])]:
        correct += 1
print("Accuracy: ", correct / total)

# print(sum(sum(row) for row in data['4_airplane.png'][classes.index('airplane')]))
# print(sum(sum(row) for row in data['4_airplane.png'][classes.index('frog')]))
# print('--------------------')
# print(sum(sum(row) for row in data['5_frog.png'][classes.index('frog')]))
# print(sum(sum(row) for row in data['5_frog.png'][classes.index('deer')]))
# print('--------------------')
# print(sum(sum(row) for row in data['10_automobile.png'][classes.index('automobile')]))
# print(sum(sum(row) for row in data['10_automobile.png'][classes.index('truck')]))
# print('--------------------')


# print(img_id)
# print(targets)

# print(len(data['1_cat.png'][0][0]))
# data['1_cat.png'][0]