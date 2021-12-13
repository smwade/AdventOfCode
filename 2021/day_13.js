
import { promises as fs } from 'fs'


const parseInput = async () => {
  let data = await (await fs.readFile('input/day_13.txt', 'utf-8'))
	data = data.split('\n')
	let points = []
	let folds = []
	for (let row of data) {
		if (row.includes('fold')) {
			row = row.slice(11).split('=')
			folds.push([row[0],+row[1]])
		} 
		else if (row !== '') {
			points.push(row.split(',').map(Number))	
		}
	}
	data = [points, folds]
  return data 
}

function printMatrix(M) {
	let s = ''
	for (let row in M) {
		s += '\n'
		for (let col in M[0]) {
			s += `${M[row][col]}`
		}	
	}
	console.log(s)
}

const part1 = async () => {
  let [points, folds] = await parseInput()
	let [dim, f] = folds[0]
	let newPoints = new Set()

	for (let [x,y] of points) {
		if (dim === 'x') {
			if (x > f) {
				x = f-(x-f)
			}
		} else {
			if (y > f) {
				y = f-(y-f)
			}
		}
		newPoints.add(`${x},${y}`)
	}
	console.log(newPoints.size)
}

const part2 = async () => {
  let [points, folds] = await parseInput()
	points = points.map(x=>`${x[0]},${x[1]}`)
	points = new Set(points)
	let xDim
	let yDim
	for (let [dim,f] of folds) {
		let newPoints = new Set()
		for (let p of points) {
			let [x,y] = p.split(',').map(x => +x)
			if (dim === 'x') {
				xDim = f
				if (x > f) {
					x = f-(x-f)
				}
			} else {
				yDim = f
				if (y > f) {
					y = f-(y-f)
				}
			}
			newPoints.add(`${x},${y}`)
		}
		points = newPoints
	}
	// display the codes
	let arr = new Array(yDim).fill('.').map(() => Array(xDim).fill('.'))
	points = [...points].map(x=>x.split(',').map(y => +y))
	for (let [x,y] of points) {
		arr[y][x] = '*'	
	}
	printMatrix(arr)
}

part2()
