
import { promises as fs } from 'fs'


const parseInput = async () => {
  let infile = process.argv.length > 2 ? process.argv[2] : 'input/day_9.txt'
  let data = await fs.readFile(infile, 'utf-8')
  return data.split('\n')
    .map(x => x.split(''))
    .map(x => x.map(Number))
}

const part1 = async () => {
  const data = await parseInput()
  let riskVals = []
  for (let row = 0; row < data.length; row++) {
    for (let col = 0; col < data[row].length; col++) {
      let val = data[row][col]
      let neighbors = []
      if (row-1 >= 0) neighbors.push([row-1,col])
      if (row+1 < data.length) neighbors.push([row+1,col])
      if (col-1 >= 0) neighbors.push([row,col-1])
      if (col+1 < data[row].length) neighbors.push([row,col+1])
      let isLow = true
      for (const [nRow, nCol] of neighbors) {
        if (data[nRow][nCol] <= val) {
          isLow = false
        }
      }
      if (isLow) riskVals.push(val+1)
    }
  }
  return riskVals.reduce((a,b) => a+b)
}


const getNeighbors = (arr, row, col) => {
  let neighbors = []
  if (row-1 >= 0) neighbors.push([row-1,col])
  if (row+1 < arr.length) neighbors.push([row+1,col])
  if (col-1 >= 0) neighbors.push([row,col-1])
  if (col+1 < arr[row].length) neighbors.push([row,col+1])
  return neighbors
}

const part2 = async () => {
  const data = await parseInput()

  // get the lowest points of the basin
  let lowPoints = []
  for (let row = 0; row < data.length; row++) {
    for (let col = 0; col < data[row].length; col++) {
      let val = data[row][col]
      let neighbors = getNeighbors(data, row, col)
      let isLow = true
      for (const [nRow, nCol] of neighbors) {
        if (data[nRow][nCol] <= val) {
          isLow = false
        }
      }
      if (isLow) lowPoints.push([row, col])
    }
  }

  // do a search to get points in basin
  let [row, col] = lowPoints[0]




}


part2().then(console.log)
