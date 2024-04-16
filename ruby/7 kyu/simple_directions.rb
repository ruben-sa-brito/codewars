#https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca
def solve arr

    direction_inversion = {'Right' => 'Left', 'Left' => 'Right'}
    paths = ['Begin ' + arr[-1].split(' ', 2)[1]]
    direction = arr[-1].split(' ', 2)[0]

    arr.reverse[1..].each do |road|

        direction_road = road.split(' ', 2)
        paths << direction_inversion[direction] + ' ' + direction_road[1]
        direction = road.split(" ", 2)[0]

    end

    paths 

end