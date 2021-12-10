
import { promises as fs } from 'fs'


const parseInput = async () => {
  let data = await fs.readFile('input/day_10.txt', 'utf-8')
  return data.split('\n')
}

const cScore = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

const aScore = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
}

const cMap = {')':'(', ']':'[', '}':'{', '>':'<'}
const cMapOpen= {'(':')', '[':']', '{':'}', '<':'>'}
const cOpen = new Set(['(', '[', '{', '<'])


function firstError(line) {
  let stack = []
  for (const c of line) {
    if (cOpen.has(c)) {
      stack.push(c)
    } else {
      let cPop = stack.pop()
      if (cPop != cMap[c]) {
        return c
      }
    } 
  }
  if (stack.length > 0) {
    return stack
  }
  return
}


const part1 = async () => {
  const data = await parseInput()
  let badChars = []
  for (const line of data) {
    let e = firstError(line)
    if (e instanceof String) {
      badChars.push(e)
    }
  }
  console.log(badChars.filter(Boolean).map(x => cScore[x]).reduce((a,b) => a + b));
}

const part2 = async () => {
  const data = await parseInput()
  let scores = []
  for (const line of data) {
    let stack = firstError(line)
    if (!(stack instanceof Array)) continue
    let rowChars = []
    while (stack.length) {
      let c = stack.pop()
      rowChars.push(cMapOpen[c])
    }
    let score = 0
    for (const c of rowChars) {
      score = score * 5
      score += aScore[c] 
    }
    scores.push(score)
  }
  scores = scores.sort(function (a, b) {  return a - b;  });
  console.log(scores[Math.floor(scores.length/2)]) // floor becase starts at 0
}

part1()
part2()



