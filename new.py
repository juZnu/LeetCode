def solve(clawPos, boxes, boxInClaw):
    # Step 1: Get all available boxes
    sumOfBoxes = sum(boxes)
    numOfStacks = len(boxes)
    if boxInClaw:
        sumOfBoxes += 1

    # Step 2: Create a target - How the boxes should eventually be/look like
    target = [0] * numOfStacks
    while sumOfBoxes != 0:
        for i in range(numOfStacks):
            if sumOfBoxes != 0:
                target[i] += 1
                sumOfBoxes -= 1

    # Step 3: At any position, check if a box should be placed
    if boxInClaw and boxes[clawPos] < target[clawPos]:
        return 'PLACE'

    # Step 4: At any position, check if a box should be picked
    if not boxInClaw and boxes[clawPos] > target[clawPos]:
        return 'PICK'

    # Step 5: Check if should go right
    for i in range(clawPos, numOfStacks):
        if boxInClaw:
            if boxes[i] < target[i]:
                return 'RIGHT'
        else:
            if boxes[i] > target[i]:
                return 'RIGHT'

    # Step 6: Check if should go left
    for i in range(clawPos, -1, -1):
        if boxInClaw:
            if boxes[i] < target[i]:
                return 'LEFT'
        else:
            if boxes[i] > target[i]:
                return 'LEFT'

    return ''

# Example usage
def simulate():
    clawPos = 2
    boxInClaw = True
    boxes = [0, 0, 2, 0]

    while True:
        action = solve(clawPos, boxes, boxInClaw)
        print(f"Action: {action}, Claw Position: {clawPos}, Boxes: {boxes}, Box in Claw: {boxInClaw}")

        if action == 'PLACE':
            boxes[clawPos] += 1
            boxInClaw = False
        elif action == 'PICK':
            boxes[clawPos] -= 1
            boxInClaw = True
        elif action == 'RIGHT':
            clawPos += 1
        elif action == 'LEFT':
            clawPos -= 1
        else:
            print("Completed!")
            break

# Start the simulation
simulate()
