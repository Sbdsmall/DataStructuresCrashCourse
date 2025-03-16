"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var EXERCISE_LL_Constructor_1 = require("../Constructer/EXERCISE-LL-Constructor");
var LinkedListPush = /** @class */ (function (_super) {
    __extends(LinkedListPush, _super);
    function LinkedListPush() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    LinkedListPush.prototype.printList = function () {
        var temp = this.head;
        while (temp !== null) {
            console.log(temp.value);
            temp = temp.next;
        }
    };
    LinkedListPush.prototype.getHead = function () {
        if (this.head === null) {
            console.log("Head: null");
        }
        else {
            console.log("Head: " + this.head.value);
        }
    };
    LinkedListPush.prototype.getTail = function () {
        if (this.tail === null) {
            console.log("Tail: null");
        }
        else {
            console.log("Tail: " + this.tail.value);
        }
    };
    LinkedListPush.prototype.getLength = function () {
        console.log("Length: " + this.length);
    };
    LinkedListPush.prototype.makeEmpty = function () {
        this.head = null;
        this.tail = null;
        this.length = 0;
    };
    /// WRITE PUSH METHOD HERE ///
    //                          //
    //                          //
    //                          //
    //                          //
    //////////////////////////////
    LinkedListPush.prototype.push = function (val) {
        var newNode = new EXERCISE_LL_Constructor_1.Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            //@ts-ignore
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return this;
    };
    return LinkedListPush;
}(EXERCISE_LL_Constructor_1.LinkedList));
function test() {
    var myLinkedList = new LinkedListPush(1);
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
