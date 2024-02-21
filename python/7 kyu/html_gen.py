#https://www.codewars.com/kata/54eecc187f9142cc4600119e
class HTMLGen:
    
    def a(self, in_html):
        
        return '<a>'+in_html+'</a>'
    
    def b(self, in_html):
        
        return '<b>'+in_html+'</b>'
    
    def p(self, in_html):
        
        return '<p>'+in_html+'</p>'
    
    def body(self, in_html):
        
        return '<body>'+in_html+'</body>'
    
    def div(self, in_html):
        
        return '<div>'+in_html+'</div>'
    
    def span(self, in_html):
        
        return '<span>'+in_html+'</span>'
    
    def title(self, in_html):
        
        return '<title>'+in_html+'</title>'
    
    def comment(self, in_html):
        
        return '<!--'+in_html+'-->'      