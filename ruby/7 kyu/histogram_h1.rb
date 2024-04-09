def histogram(results)

  hist = ""
  dice = (1..6).to_a.reverse

  for face, plays in dice.zip(results.reverse)
    if plays == 0
      hist += "#{face}|" + "#"*plays + "\n"
    else
      hist += "#{face}|" + "#"*plays + " #{plays}\n"
    end
  end

  hist

end
