# -*- coding: utf-8 -*-
# لعبة أسئلة وأجوبة بمراحل للمراهقين - بالعربية

levels = {
    "سهل": [
        {
            "question": "ما هي عاصمة المملكة العربية السعودية؟",
            "options": ["أ) جدة", "ب) الرياض", "ج) الدمام", "د) مكة"],
            "answer": "ب"
        },
        {
            "question": "كم يساوي 5 + 7 ؟",
            "options": ["أ) 10", "ب) 11", "ج) 12", "د) 13"],
            "answer": "ج"
        },
        {
            "question": "من هو مخترع المصباح الكهربائي؟",
            "options": ["أ) توماس إديسون", "ب) نيوتن", "ج) آينشتاين", "د) غاليليو"],
            "answer": "أ"
        },
        {
            "question": "أي من التالي يعتبر كوكبًا؟",
            "options": ["أ) بلوتو", "ب) القمر", "ج) المشتري", "د) الشمس"],
            "answer": "ج"
        }
    ],
    "متوسط": [
        {
            "question": "في أي دولة تقع مدينة طوكيو؟",
            "options": ["أ) الصين", "ب) كوريا الجنوبية", "ج) اليابان", "د) سنغافورة"],
            "answer": "ج"
        },
        {
            "question": "ما هو أطول نهر في العالم؟",
            "options": ["أ) النيل", "ب) الأمازون", "ج) دجلة", "د) الفرات"],
            "answer": "أ"
        },
        {
            "question": "من الصحابي الملقّب بالفاروق؟",
            "options": ["أ) أبو بكر الصديق", "ب) عمر بن الخطاب", "ج) علي بن أبي طالب", "د) عثمان بن عفان"],
            "answer": "ب"
        },
        {
            "question": "في الأنمي الشهير 'ناروتو'، ما هو اسم وحش الذيول داخل ناروتو؟",
            "options": ["أ) كوراما", "ب) شيوكاكو", "ج) مادارا", "د) جيرايا"],
            "answer": "أ"
        }
    ],
    "صعب": [
        {
            "question": "في الفيزياء، ما هو القيمة التقريبية لتسارع الجاذبية الأرضية؟",
            "options": ["أ) 6.8 m/s²", "ب) 8.9 m/s²", "ج) 9.8 m/s²", "د) 10.8 m/s²"],
            "answer": "ج"
        },
        {
            "question": "من هو مؤلف رواية 'البؤساء'؟",
            "options": ["أ) فيكتور هوغو", "ب) تشارلز ديكنز", "ج) شكسبير", "د) دوستويفسكي"],
            "answer": "أ"
        },
        {
            "question": "أي من هذه الدول ليست عربية؟",
            "options": ["أ) تونس", "ب) تركيا", "ج) قطر", "د) لبنان"],
            "answer": "ب"
        },
        {
            "question": "في كرة القدم، كم لاعب أساسي في كل فريق داخل الملعب؟",
            "options": ["أ) 9", "ب) 10", "ج) 11", "د) 12"],
            "answer": "ج"
        }
    ]
}


def ask_question(question_data):
    """تظهر سؤال واحد وتتحقق من الإجابة، وتعيد True إذا كانت صحيحة"""
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)

    user_answer = input("اكتب حرف الإجابة (أ / ب / ج / د): ").strip().lower()
    correct_answer = question_data["answer"].strip().lower()

    if user_answer == correct_answer:
        print("✅ إجابة صحيحة!")
        return True
    else:
        print(f"❌ إجابة خاطئة! الإجابة الصحيحة هي: {question_data['answer']}")
        return False


def play_level(level_name, questions):
    """تشغيل مرحلة كاملة، تعيد عدد الإجابات الصحيحة"""
    print("\n" + "=" * 40)
    print(f"📍 المرحلة: {level_name}")
    print("=" * 40)

    score = 
    total = len(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\nالسؤال رقم {i} من {total}:")
        if ask_question(q):
            score += 1

    print(f"\n📊 انتهت مرحلة {level_name}!")
    print(f"نتيجتك في هذه المرحلة: {score} من {total}")
    return score, total


def main():
    print("🎮 أهلاً بك في لعبة: تحدي المعلومات - بمراحل!")
    print("مكس أسئلة: أنمي، أفلام، علوم، دين، رياضة، معلومات عامة.")
    print("أجب عن الأسئلة بالاختيار من (أ / ب / ج / د)\n")

    total_score = 
    total_questions = 

    ordered_levels = ["سهل", "متوسط", "صعب"]

    for level_name in ordered_levels:
        questions = levels[level_name]
        score, total = play_level(level_name, questions)

        total_score += score
        total_questions += total

        if score < total // 2:
            print(f"\n❗ لم تحصل على عدد كافٍ من الإجابات الصحيحة للانتقال من مرحلة {level_name}.")
            print("جرّب اللعب مرة أخرى لتحسن نتيجتك. 🙂")
            break
        else:
            print(f"\n✅ أحسنت! يمكنك الانتقال من مرحلة {level_name} إلى المرحلة التالية!")
            if level_name == ordered_levels[-1]:
                print("\n🏁 لقد وصلت إلى نهاية جميع المراحل!")

    print("\n" + "#" * 40)
    print("📌 ملخص اللعبة:")
    print(f"إجمالي نتيجتك: {total_score} من {total_questions}")
    if total_questions > :
        نسبة = (total_score / total_questions) * 100
        print(f"نسبة النجاح: {نسبة:.1f}%")
    print("#" * 40)

    if total_questions > :
        if total_score == total_questions:
            print("🔥 أسطوري! جاوبت على كل الأسئلة بشكل صحيح!")
        elif total_score >= total_questions * .6:
            print("👏 أداء ممتاز، معلوماتك قوية!")
        elif total_score >= total_questions * .4:
            print("🙂 أداء مقبول، تحتاج شوية تطوير.")
        else:
            print("💡 لا بأس، اعتبرها بداية وطوّر نفسك أكثر.")


if __name__ == "__main__":
    main()
