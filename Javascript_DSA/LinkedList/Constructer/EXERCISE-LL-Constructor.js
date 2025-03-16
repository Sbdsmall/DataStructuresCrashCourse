"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.LinkedList = exports.Node = void 0;
// WRITE NODE CLASS HERE //
//                       //
//                       //
//                       //
//                       //
///////////////////////////
var Node = /** @class */ (function () {
    function Node(value) {
        this.value = value;
        this.next = null;
    }
    return Node;
}());
exports.Node = Node;
var LinkedList = /** @class */ (function () {
    function LinkedList(val) {
        this.length = 0;
        var newNode = new Node(val);
        this.head = newNode;
        this.tail = this.head;
        this.length = 1;
    }
    LinkedList.prototype.printList = function () {
        var temp = this.head;
        while (temp !== null) {
            console.log(temp.value);
            temp = temp.next;
        }
    };
    LinkedList.prototype.getHead = function () {
        if (this.head === null) {
            console.log("Head: null");
        }
        else {
            console.log("Head: " + this.head.value);
        }
    };
    LinkedList.prototype.getTail = function () {
        if (this.tail === null) {
            console.log("Tail: null");
        }
        else {
            console.log("Tail: " + this.tail.value);
        }
    };
    LinkedList.prototype.getLength = function () {
        console.log("Length: " + this.length);
    };
    return LinkedList;
}());
exports.LinkedList = LinkedList;
function test() {
    var myLinkedList = new LinkedList(4);
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
    Head: 4
    Tail: 4
    Length: 1
    
    Linked List:
    4

*/ 
