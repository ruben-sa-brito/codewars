def decompose_single_strand(single_strand):
    
    
    decompose_frame_1 = [single_strand[x-3:x] for x, l in enumerate(single_strand) if x % 3 == 0 and x!=0 ]
    decompose_frame_1.append(single_strand[-3:])
    
    decompose_frame_2 = [single_strand[1:-2][x-3:x] for x, l in enumerate(single_strand[1:-2]) if x % 3 == 0 and x!=0 ]
    decompose_frame_2.append(single_strand[1:-2][-3:])
    decompose_frame_2.insert(0, single_strand[0])
    decompose_frame_2.append( single_strand[-2:])
    if '' in decompose_frame_2: decompose_frame_2.remove('')
    
    decompose_frame_3 = [single_strand[2:-1][x-3:x] for x, l in enumerate(single_strand[2:-1]) if x % 3 == 0 and x!=0 ]
    decompose_frame_3.append(single_strand[2:-1][-3:])
    decompose_frame_3.insert(0, single_strand[0:2])
    decompose_frame_3.append( single_strand[-1])
    if '' in decompose_frame_3: decompose_frame_3.remove('')
    
    
    return 'Frame 1: '+' '.join(decompose_frame_1) +'\n'+ 'Frame 2: '+' '.join(decompose_frame_2) + '\n'+ 'Frame 3: '+' '.join(decompose_frame_3)