
import { promises as fs } from 'fs'


const parseInput = async () => {
  let data = await fs.readFile('input/day_8.txt', 'utf-8')
  return data
}

const part1 = async () => {
  const data = await parseInput()
	console.log("asdf")
}

part1()
