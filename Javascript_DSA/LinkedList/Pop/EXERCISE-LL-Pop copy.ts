import { LinkedList, Node } from "../Constructer/EXERCISE-LL-Constructor";

 
class LinkedListPop extends LinkedList{

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
 
    push(value) {
        const newNode = new Node(value);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            // @ts-ignore
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return this;
    }
 
	/// WRITE POP METHOD HERE ///
	//                         //
	//                         //
	//                         //
	//                         //
	/////////////////////////////
    
    pop(): Node | null {
        const poppedNode = this.tail;
        if (!this.head) {
            console.log("There is no data in this linked list")
            return null
        } else {

        }
        return poppedNode
    }
 }
 

 function test() {
    let myLinkedList = new LinkedListPop(1);
    myLinkedList.push(2);

    // (2) Items in LL - Returns 2 Node
    if (myLinkedList.length !== 0) {
        console.log(myLinkedList.pop().value);
    } else {
        console.log("null");
    }

    // (1) Item in LL - Returns 1 Node
    if (myLinkedList.length !== 0) {
        console.log(myLinkedList.pop().value);
    } else {
        console.log("null");
    }

    // (0) Items in LL - Returns null
    if (myLinkedList.length !== 0) {
        console.log(myLinkedList.pop().value);
    } else {
        console.log("null");
    }
 }


 test();


/*
    EXPECTED OUTPUT:
    ----------------
    2
    1
    null

*/