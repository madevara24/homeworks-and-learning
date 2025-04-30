package main

import (
	"leetcode/lru"
)

const LIMIT = 4

func main() {
	n := make(map[int]*lru.Node)
	cache := lru.Lru{
		Limit: LIMIT,
		Nodes: n,
	}

	cache.Put(1, "1")
	cache.Put(2, "2")
	cache.Get(1)
	cache.Put(3, "3")
	cache.Put(4, "4")
	cache.Put(5, "5")
	cache.Get(3)
	cache.Get(7)
	cache.Get(1)
	cache.Put(6, "6")
	cache.Put(7, "7")
	cache.Get(7)

}
