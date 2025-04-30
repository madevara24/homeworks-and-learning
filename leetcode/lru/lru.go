package lru

import "fmt"

type Lru struct {
	Limit int
	Head  *Node
	Tail  *Node
	Nodes map[int]*Node
}

type Node struct {
	Value interface{}
	Prev  *Node
	Next  *Node
}

func (l *Lru) Put(key int, value interface{}) {
	if _, ok := l.Nodes[key]; ok {
		l.Nodes[key].Value = value

		fmt.Println("Assigning ", l.Nodes[key].Value, " on existing node...")

		l.MoveToHead(l.Nodes[key])
		return
	}

	l.Nodes[key] = &Node{
		Value: value,
	}

	fmt.Println("Assigning ", l.Nodes[key].Value, " as new node...")

	if l.Head != nil {
		l.Nodes[key].Next = l.Head
		l.Head.Prev = l.Nodes[key]
	}

	l.Head = l.Nodes[key]

	if l.Tail == nil {
		l.Tail = l.Nodes[key]
	}

	l.PrettyPrint()

	if len(l.Nodes) > l.Limit {
		fmt.Println("Cache reached limit...")
		l.PopTail()
	}
}

func (l *Lru) Get(key int) interface{} {
	fmt.Println("Fetcing ", key, "...")
	if node, ok := l.Nodes[key]; ok {
		fmt.Println("Found ", node.Value, " in ", key, "...")
		l.MoveToHead(node)
		return node
	}
	fmt.Println("Key ", key, " not found...")
	return nil
}

func (l *Lru) PopTail() {
	if l.Tail.Prev != nil {
		fmt.Println("Popping ", l.Tail.Value)
		l.Tail = l.Tail.Prev
		l.Tail.Next = nil
		l.PrettyPrint()
	} else {
		fmt.Println("No more node to replace tail...")
	}
}

func (l *Lru) GetTail() interface{} {
	return l.Tail.Value
}

func (l *Lru) GetHead() interface{} {
	return l.Head.Value
}

func PrintNodesBackward(n *Node) {
	fmt.Println(n.Value)
	if n.Next != nil {
		PrintNodesBackward(n.Next)
	} else {
		fmt.Println("Already at tail, no more node to print...")
	}
}

func PrintNodesForward(n *Node) {
	fmt.Println(n.Value)
	if n.Prev != nil {
		PrintNodesForward(n.Prev)
	} else {
		fmt.Println("Already at head, no more node to print...")
	}
}

func (l *Lru) MoveToHead(n *Node) {
	// HEAD
	// ONLY NEED TO CHANGE SEQUNCE WHEN IT'S NOT THE HEAD
	if n.Prev != nil {
		oldPrev := n.Prev
		oldNext := n.Next

		// IF N IS THE TAIL
		if oldNext == nil {
			fmt.Println(n.Value, " is the tail, moving ", oldPrev.Value, " to become the new tail...")
			// OLD PREV BECOMES THE TAIL
			oldPrev.Next = nil
			l.Tail = oldPrev
		} else
		// IF N IS NOT THE TAIL
		{
			fmt.Println(n.Value, " is between ", oldPrev.Value, " and ", oldNext.Value, ", joining them together...")
			// SEVERE THE TIE FOR N AND JOIN THE NODES ON EACH SIDE
			oldPrev.Next = oldNext
			oldNext.Prev = oldPrev
		}

		fmt.Println("Replacing ", l.Head.Value, " as head with ", n.Value)

		n.Prev = nil
		n.Next = l.Head
		l.Head.Prev = n
		l.Head = n
	} else {
		fmt.Println(n.Value, " is the head, no need for rearrangement...")
	}

	l.PrettyPrint()
}

func (l *Lru) PrettyPrint() {
	fmt.Println("==================================================")
	fmt.Println("Head -> Tail:")
	current := l.Head
	for current != nil {
		fmt.Printf("Node{Value: %v} ", current.Value)
		if current.Next != nil {
			fmt.Print("-> ")
		}
		current = current.Next
	}
	fmt.Println("\nTail -> Head:")
	current = l.Tail
	for current != nil {
		fmt.Printf("Node{Value: %v} ", current.Value)
		if current.Prev != nil {
			fmt.Print("-> ")
		}
		current = current.Prev
	}
	fmt.Println()
	fmt.Println("==================================================")
}
