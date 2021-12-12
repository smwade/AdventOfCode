
import { promises as fs } from 'fs'


const parseInput = async () => {
  let M = await fs.readFile('input/day_11.txt', 'utf-8')
  return M.split('\n')
    .map(x => x.split('').map(x => +x.trim()))
}

const main = async () => {
  let M = await parseInput()
  let n = M.length
  let m = M[0].length
  let flashCnt = 0

  let step = 1
  while (true) {

    let doStep = (row, col) => {
      let val = M[row][col]
      if (val === 9) {
        M[row][col] = -1
        flashCnt += 1
        for (let r = row-1; r <= row+1; r++) {
          for (let c = col-1; c <= col+1; c++) {
            if (r < n && r >= 0 && c < m && c >= 0) {
              doStep(r,c)
            }
          }
        }
      } 
      else if (val !== -1) {
        M[row][col] = val + 1
      }
    }

    for (let row=0; row < M.length; row++) {
      for (let col=0; col < M.length; col++) {
        doStep(row, col)
      }
    }
    
    let allFlashed = true
    for (let row=0; row < M.length; row++) {
      for (let col=0; col < M.length; col++) {
        if ( M[row][col] === -1 ) {
          M[row][col] = 0
        } else {
          allFlashed = false
        }
      }
    }  
    if (allFlashed) return step
    step++
  }
}

main().then(console.log)
