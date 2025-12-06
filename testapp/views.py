from django.shortcuts import render

# Question class
class Questions:
    def __init__(self, que, a, b, c, d, correct, explanation):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct  # answer: 'a', 'b', 'c', 'd'
        self.explanation = explanation


def testpaper(request):
    questions = [
        Questions(
            'जीविक वर्गीकरण की सबसे छोटी मूल इकाई कौन-सी है?',
            '(a) संघ (Genus)', '(b) कुल (Family)', '(c) जाति / प्रजाति (Species)', '(d) गण (Order)',
            'c',
            'Species (जाति) ही सबसे छोटी वर्गीकरण इकाई होती है।'
        ),


        Questions(
            'Panthera tigris (बाघ) और Panthera leo (शेर) में कौन-सी श्रेणी समान होती है?',
            '(a) Species (जाति)', '(b) Genus (वंश)', '(c) Family (कुल)', '(d) Order (गण)',
            'b',
            'दोनों का वंश Panthera है, इसलिए Genus समान है।'
        ),


        Questions(
            'Felis domesticus (बिल्ली) और Panthera pardus (तेंदुआ) किस श्रेणी में समान हैं?',
            '(a) वंश', '(b) कुल', '(c) गण', '(d) जाति',
            'b',
            'दोनों का कुल Felidae है।'
        ),


        Questions(
            'मनुष्य (Homo sapiens) किस वर्ग में आते हैं?',
            '(a) Aves (पक्षी)', '(b) Mammalia (स्तनधारी)', '(c) Reptilia (सरीसृप)', '(d) Amphibia (उभयचर)',
            'b',
            'मनुष्य स्तनधारी (Mammalia) वर्ग में आते हैं।'
        ),


        Questions(
            'Primates और Carnivora किस टैक्सोनिक श्रेणी के अंतर्गत आते हैं?',
            '(a) वर्ग (Class)', '(b) गण (Order)', '(c) संघ (Phylum)', '(d) कुल (Family)',
            'a',
            'Primates और Carnivora दोनों Mammalia वर्ग के अंतर्गत आते हैं।'
        ),


        Questions(
            'एक ही Family (कुल) में आने वाले जीवों में क्या समान होता है?',
            '(a) वे आपस में संकरण कर सकते हैं', '(b) उनके कई वंशों में समान गुण होते हैं',
            '(c) सभी Species एक जैसी होती हैं', '(d) वे अलग-अलग Class में आते हैं',
            'b',
            'एक ही कुल के जीवों में कई समान लक्षण पाए जाते हैं।'
        ),


        Questions(
            'Homo और Panthera में कौन-सी श्रेणी समान है?',
            '(a) कुल', '(b) गण', '(c) वर्ग', '(d) वंश',
            'c',
            'दोनों वर्ग Mammalia में आते हैं।'
        ),


        Questions(
            'सही वर्गीकरण क्रम क्या है?',
            '(a) वर्ग → संघ → गण → कुल', '(b) संघ → वर्ग → गण → कुल',
            '(c) गण → वर्ग → कुल → संघ', '(d) कुल → संघ → गण → वर्ग',
            'b',
            'सही क्रम है: संघ → वर्ग → गण → कुल'
        ),

        Questions(
            'सबसे अधिक समानता किस श्रेणी में पाई जाती है?',
            '(a) गण', '(b) कुल', '(c) जाति/Species', '(d) वर्ग',
            'c',
            'सबसे अधिक समानता Species स्तर पर पाई जाती है।'
        ),




    ]

    # If student submits the test
    if request.method == "POST":
        score = 0
        detailed_result = []

        for i, q in enumerate(questions, 1):
            selected_option = request.POST.get(f'option{i}')

            if selected_option == q.correct:
                score += 1

            detailed_result.append({
                'question': q.que,
                'options': [q.a, q.b, q.c, q.d],
                'correct': q.correct,
                'selected': selected_option,
                'explanation': q.explanation
            })

        total = len(questions)
        percentage = round((score / total) * 100, 1)

        context = {
            'score': score,
            'total': total,
            'percentage': percentage,
            'result': detailed_result
        }
        return render(request, 'result.html', context)

    return render(request, 'question.html', {'questions': questions})