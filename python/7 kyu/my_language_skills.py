class FilterLanguages:
    def __call__(self, results):
        return [lang for lang, score in sorted(results.items(), key=lambda item: item[1] , reverse=True) if results[lang]>=60]

my_languages = FilterLanguages()