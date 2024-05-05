#https://www.codewars.com/kata/53b7bc844db8fde50800020a
require 'set'
def on_line(points)
    points = Set.new(points).to_a
    begin
      
        point_ref = points[1]
        m = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]).to_f
        
        points[2..-1].each do |point|
            debugger
            if ((point[1] - point_ref[1]) / (point[0] - point_ref[0]).to_f) != m
                return false
            end    
        end
        true
    rescue
        true
    end  
end