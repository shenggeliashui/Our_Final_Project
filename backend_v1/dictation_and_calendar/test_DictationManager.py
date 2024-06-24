from DictationManager import DictationManager

def test_dictation_manager():
    book_id = "CET4"  # 替换为实际的book_id
    dictation_manager = DictationManager()

    # 测试获取随机单词
    print("获取随机单词...")
    dictation_manager.fetch_random_words(book_id)
    if not dictation_manager.words_info:
        print("获取随机单词失败")
        return

    print("成功获取随机单词")
    
    # 测试逐个获取单词并移动到下一个单词
    while True:
        current_word = dictation_manager.get_current_word()
        if not current_word:
            break
        
        print(f"\n当前单词信息: {current_word}")

        # 获取单词音标
        usphone, ukphone = dictation_manager.get_phonetics()
        print(f"美式音标: {usphone}")
        print(f"英式音标: {ukphone}")

        # 获取单词本身
        word = dictation_manager.get_word()
        print(f"单词: {word}")

        # 获取词性和释义
        pos_and_tran = dictation_manager.get_pos_and_tran()
        print(f"词性和释义: {pos_and_tran}")

        # 获取例句
        example = dictation_manager.get_example()
        print(f"例句: {example['sContent']}")
        print(f"例句翻译: {example['sCn']}")

        # 测试是否匹配输入单词
        input_word = input(f"请默写单词 '{word}': ").strip()
        match, correct_word = dictation_manager.is_word_match(input_word)
        if match:
            print("默写正确!")
        else:
            print(f"默写错误! 正确的单词是: {correct_word}")

        if not dictation_manager.move_to_next_word():
            break

    # 销毁实例
    del dictation_manager

if __name__ == "__main__":
    test_dictation_manager()

