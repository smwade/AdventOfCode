
import { promises as fs } from 'fs'


const parseInput = async () => {
  let data = await (await fs.readFile('input/day_12.txt', 'utf-8'))
                .split('\n')
  let G = {}
  for (const row of data) {
    let [n1, n2] = row.split('-')
    if (!(n1 in G)) G[n1] = [];
    if (!(n2 in G)) G[n2] = [];
    G[n1].push(n2)
    G[n2].push(n1)
  }
  return G 
}


const part1 = async () => {
  let G = await parseInput()
  let allPaths = []

  const search = (node, path) => {
    if (node === 'end') {
      allPaths.push([...path])
      return
    }
    for (let neighbor of G[node]) {
      if (!(path.includes(neighbor) && neighbor === neighbor.toLowerCase())) {
        search(neighbor, [...path, neighbor])
      }
    }
  }

  search('start', ['start'])
  return allPaths.length
}


const isSmallCave = (s) => {
  return s === s.toLowerCase()
    && s !== 'start'
    && s !== 'end'
}

const part2 = async () => {
  let G = await parseInput()
  let allPaths = []

  const search = (node, path, visitedSmallCave) => {
    if (node === 'end') {
      allPaths.push([...path,node])
      return
    }
    for (let neighbor of G[node]) {
      if (neighbor === 'start') continue
      else if (isSmallCave(node) && path.includes(node) && visitedSmallCave) continue
      else if (isSmallCave(node) && path.includes(node) && !visitedSmallCave) {
        search(neighbor, [...path,node], true)
      }
      else {
        search(neighbor, [...path,node], visitedSmallCave)
      }
    }
  }

  search('start', [])
  return allPaths.length
}

part1().then(console.log)
part2().then(console.log)