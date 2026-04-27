# 🐍 Snake AI with Genetic Algorithm

Artificial Intelligence project using **Neural Networks** and a **Genetic Algorithm** to train a snake to play Snake automatically.

The AI learns through genetic evolution, without datasets or supervised training. Each generation improves based on the performance of the best neural networks.

---

## 🚀 Technologies Used

- Python 3
- Pygame
- Neural Networks from scratch
- Genetic Algorithm
- Pickle (population persistence)

---

## 🧠 How It Works

The AI controls the snake using a simple neural network.

### Network Inputs (10 inputs)

The network receives information from the environment:

- Danger ahead
- Danger to the left
- Danger to the right
- Food ahead
- Food to the left
- Food to the right
- Current snake direction:
  - left
  - right
  - up
  - down

### Network Outputs (3 outputs)

The network decides between:

- Turn left
- Move forward
- Turn right

---

## 🧬 Genetic Algorithm

The evolution process works as follows:

1. A population of neural networks is created
2. Each network plays a game
3. The best networks are selected
4. Copies receive random mutations
5. A new generation is created
6. The process repeats indefinitely

---

## 📊 Fitness Function

```python
fitness = (score * 100 + steps * 0.5 - hunger * 2)
```

The AI is rewarded for:

- Eating food
- Surviving longer

And penalized for:

- Staying too long without eating

---

## 📁 Project Structure

```bash
project/
│
├── neural_network/
│   ├── genetic.py          # Main genetic algorithm
│   ├── network.py          # Neural network structure
│   └── neuron.py           # Neuron implementation
│
├── game/
│   ├── snake.py            # Game logic
│   ├── player.py           # Player object
│   ├── block.py            # Block object
│   └── food.py             # Food object
│
├── requirements.txt        # Dependencies
└── README.md               # README file
```

---

## ⚙️ Network Structure

```python
[10, 16, 3]
```

- 10 input neurons
- 16 hidden neurons
- 3 output neurons

---

## 💾 Automatic Saving

The population is automatically saved using `pickle`.

Generated files:

- `neural_network.pkl`
- `structure.pkl`

When the project starts again, training continues from the last saved generation.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Enter the project folder

```bash
cd your-repository
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python genetic.py
```

---

## 📈 Displayed Metrics

During training:

- Current generation
- Current network
- Best overall fitness
- Best overall score
- Best generation fitness
- Best generation score

---

## 🔥 Possible Future Improvements

- Network crossover
- Adaptive mutation
- More vision sensors
- Deep neural networks
- Population parallelization
- Replay system for best games
- Fast training without rendering
- Metrics export
- Graphical evolution visualization

---

## 📚 Concepts Applied

This project uses concepts from:

- Artificial Intelligence
- Machine Learning
- Neuroevolution
- Genetic Algorithms
- Neural Networks
- Object-Oriented Programming

---

## 🧪 Example of Evolution

At every generation:

- The best snakes survive
- Weak networks are discarded
- New networks emerge through mutations
- The behavior gradually improves

Over time, the AI learns to:

- Avoid walls
- Avoid its own body
- Find food
- Survive longer

---

## 👨‍💻 Author

Developed by Vinicius Lemes.
