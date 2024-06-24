import random
from random_words import get_random_words_info, get_current_word, update_cursor
from word_info import get_word_example, get_word_meaning, get_word_phonetic

def test_memory_process(book_id):
    # Step 1: 获取随机单词
    print("获取随机单词信息...")
    if get_random_words_info(book_id):
        print("成功获取随机单词信息")
    else:
        print("获取随机单词信息失败")
        return
    
    while True:
        # Step 2: 获取当前单词
        current_word = get_current_word()
        if not current_word:
            print("没有更多的单词")
            break
        
        word, book_id = current_word
        print(f"\n当前单词: {word}")

        # Step 3: 获取单词例句
        example = get_word_example(word, book_id)
        if example:
            print(f"例句: {example['sContent']}")
            print(f"例句翻译: {example['sCn']}")
        else:
            print("获取单词例句失败")

        # Step 4: 获取单词词义
        meaning = get_word_meaning(word, book_id)
        if meaning:
            print("词义:")
            for pos, translations in meaning.items():
                print(f"{pos}: {', '.join(translations)}")
        else:
            print("获取单词词义失败")

        # Step 5: 获取单词音标
        phonetics = get_word_phonetic(word, book_id)
        if phonetics:
            print(f"美式音标: {phonetics[0]}")
            print(f"英式音标: {phonetics[1]}")
        else:
            print("获取单词音标失败")

        # 模拟用户输入
        user_input = input(f"请默写单词 '{word}': ").strip()

        # Step 6: 检查用户输入
        correct = user_input == word
        if correct:
            print("默写正确!")
        else:
            print("默写错误!")

        # Step 7: 更新游标，获取下一个单词
        next_word = update_cursor()
        if not next_word:
            print("没有更多的单词")
            break

if __name__ == "__main__":
    book_id = "YOUR_BOOK_ID"  # 替换为实际的book_id
    test_memory_process(book_id)

