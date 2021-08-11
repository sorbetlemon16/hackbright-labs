const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';
const WORDS = [
  'strawberry',
  'orange',
  'apple',
  'banana',
  'pineapple',
  'kiwi',
  'peach',
  'pecan',
  'eggplant',
  'durian',
  'peanut',
  'chocolate',
];

let numWrong = 0;

// Loop over the chars in `word` and create divs.
//
const createDivsForChars = (word) => {
  for (const char of word) {
    const div = document.createElement('div');
    div.classList.add('letter-box');
    div.classList.add(char);

    document.querySelector('#word-container').append(div);
  }
};

// Loop over each letter in `ALPHABET` and generate buttons.
//
const generateLetterButtons = () => {
  for (const char of ALPHABET) {
    const btn = document.createElement('button');
    btn.classList.add(char);
    btn.innerHTML = char;

    document.querySelector('#letter-buttons').append(btn);
  }
};

// Set the `disabled` property of `buttonEl` to `true.
//
// `buttonEl` is an `HTMLElement` object.
//
const disableLetterButton = (buttonEl) => {
  buttonEl.setAttribute('disabled', true);
};

// Return `true` if `letter` is in the word.
//
const isLetterInWord = (letter) => {
  return document.querySelector(`div.${letter}`) !== null;
};

// Called when `letter` is in word. Update contents of divs with `letter`.
//
const handleCorrectGuess = (letter) => {
  const letterDivs = document.querySelectorAll(`div.${letter}`);
  for (const div of letterDivs) {
    div.innerHTML = letter;
  }
};

// Called when `letter` is not in word.
//
// If the shark gets the person, disable all buttons and show the "play again"
// message. Otherwise, increment `numWrong` and update the shark image.
//
const handleWrongGuess = () => {
  numWrong += 1;

  document
    .querySelector('#shark-img img')
    .setAttribute('src', `/static/images/guess${numWrong}.png`);

  if (numWrong === 5) {
    const buttons = document.querySelectorAll('buttons');

    for (const btn of buttons) {
      btn.setAttribute('disabled', true);
    }

    document.querySelector('#play-again').style.display = '';
  }
};

//  Reset game state. Called before restarting the game.
//
const resetGame = () => {
  window.location = '/sharkwords';
};

// This is like if __name__ == '__main__' in Python
//
(function startGame() {
  // For now, we'll hardcode the word that the user has to guess.
  const word = 'hello';

  createDivsForChars(word);
  generateLetterButtons();

  document.querySelectorAll('button').forEach((btn) => {
    btn.addEventListener('click', (evt) => {
      const clickedBtn = evt.target;
      disableLetterButton(clickedBtn);

      const letter = clickedBtn.innerHTML;

      if (isLetterInWord(letter)) {
        handleCorrectGuess(letter);
      } else {
        handleWrongGuess(letter);
      }
    });
  });

  document.querySelector('#play-again').addEventListener('click', () => {
    resetGame();
  });
})();
