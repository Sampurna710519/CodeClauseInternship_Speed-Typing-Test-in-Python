import random
import time

def generate_random_sentence(words, length):
    sentence = ' '.join(random.choice(words) for _ in range(length))
    return sentence

def main():
    words = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"]
    
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    
    sentence_length = random.randint(5, 10)
    target_sentence = generate_random_sentence(words, sentence_length)
    print("Type the following sentence:")
    print(target_sentence)
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    input_time = end_time - start_time
    input_words = user_input.split()
    
    if input_words == target_sentence.split():
        words_per_minute = len(target_sentence.split()) / (input_time / 60)
        accuracy = sum(1 for a, b in zip(target_sentence.split(), input_words) if a == b) / len(target_sentence.split()) * 100
        print(f"Your typing speed: {words_per_minute:.2f} words per minute")
        print(f"Accuracy: {accuracy:.2f}%")
    else:
        print("Your input did not match the target sentence. Keep practicing!")

if __name__ == "__main__":
    main()
