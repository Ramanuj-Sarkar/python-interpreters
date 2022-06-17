#This uses normal commands, xkcd commands, and h.

num <- 0 # accumulator
keep_going <- TRUE # indicates to keep going
while(keep_going){
  # Cat prints formatted strings.
  cat('Enter code:')
  
  # You can add one whole line of code.
  # The line can include spaces and ends at a newline
  entered_code <- scan(nlines=1,what='character')
  
  # This allows the members of the character vector
  # to be interpreted as a single string.
  entered_code <- paste(entered_code, collapse = " ")
  
  # This for-loop analyses each command.
  for(pointer in 1:nchar(entered_code)){
    letter <- substr(entered_code,pointer,pointer)
    
    # This outputs each input command.
    cat(paste('>> ',letter,'\n',sep=''))
    
    if(letter %in% c("i","x")){num <- num + 1}
    else if(letter %in% c("s","k")){num <- num * num}
    else if(letter %in% c("o","c")){cat(paste(num,'\n',sep=''))}
    else if(letter == "d"){num <- num - 1}
    else if(letter == "h"){keep_going <- FALSE;break}
    
    if(num == -1 | num == 256){num <- 0}
  }
}
