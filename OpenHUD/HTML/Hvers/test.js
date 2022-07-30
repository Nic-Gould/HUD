function slidePanel() {
    if (leftPanel.style.left.valueOf()>-300) 
        {
      slideLeft();
        }
      else 
      {
      slideRight();
      }
  } 
  
  function slideLeft() {
      while (leftPanel.style.left.valueOf() > -300);
          leftPanel.style.left--;
  }

  function slideRight()	{
      while (leftPanel.style.left.valueOf < 0);
          leftPanel.style.left++;
  }