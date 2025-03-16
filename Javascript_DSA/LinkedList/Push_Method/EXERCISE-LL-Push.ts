import { LinkedList, Node } from "../Constructer/EXERCISE-LL-Constructor"

class LinkedListPush extends LinkedList {
    printList() {
        let temp = this.head;
        while (temp !== null) {
            console.log(temp.value);
            temp = temp.next;
        }
    }

    getHead() {
        if (this.head === null) {
            console.log("Head: null");
        } else {
            console.log("Head: " + this.head.value);
        }
    }

    getTail() {
        if (this.tail === null) {
            console.log("Tail: null");
        } else {
            console.log("Tail: " + this.tail.value);
        }
    }

    getLength() {
        console.log("Length: " + this.length);
    }

    makeEmpty() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
 
	/// WRITE PUSH METHOD HERE ///
	//                          //
	//                          //
	//                          //
	//                          //
	//////////////////////////////
    push(val): LinkedListPush {
        const newNode = new Node(val)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            //@ts-ignore
            this.tail.next = newNode;
            this.tail = newNode
        }
        this.length++
        
        // "this" refer to the current class instance 
        return this
    }
}
 

function test() {
    let myLinkedList = new LinkedListPush(1);
    myLinkedList.makeEmpty();
    myLinkedList.push(1);
    myLinkedList.push(2);
    
    
    myLinkedList.getHead();
    myLinkedList.getTail();
    myLinkedList.getLength();
    console.log("\nLinked List:");
    myLinkedList.printList();
}


test();


/*
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2

    Linked List:
    1
    2

*/