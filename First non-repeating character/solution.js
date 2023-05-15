const first_non_repeating_letter = str => {
  const words = str.split('');

  const firstWord = words.reduce((acc, currWord, currIndex) => {
    if (acc === '') {
      return words.some((word, index) => {
        if (currIndex !== index) return word === currWord;
      })
        ? acc
        : currWord;
    }
    return acc;
  }, '');

  return firstWord;
};
