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
var LinkedListPop = /** @class */ (function (_super) {
    __extends(LinkedListPop, _super);
    function LinkedListPop() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    LinkedListPop.prototype.printList = function () {
        var temp = this.head;
        while (temp !== null) {
            console.log(temp.value);
            temp = temp.next;
        }
    };
    LinkedListPop.prototype.getHead = function () {
        if (this.head === null) {
            console.log("Head: null");
        }
        else {
            console.log("Head: " + this.head.value);
        }
    };
    LinkedListPop.prototype.getTail = function () {
        if (this.tail === null) {
            console.log("Tail: null");
        }
        else {
            console.log("Tail: " + this.tail.value);
        }
    };
    LinkedListPop.prototype.getLength = function () {
        console.log("Length: " + this.length);
    };
    LinkedListPop.prototype.makeEmpty = function () {
        this.head = null;
        this.tail = null;
        this.length = 0;
    };
    LinkedListPop.prototype.push = function (value) {
        var newNode = new EXERCISE_LL_Constructor_1.Node(value);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            // @ts-ignore
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return this;
    };
    /// WRITE POP METHOD HERE ///
    //                         //
    //                         //
    //                         //
    //                         //
    /////////////////////////////
    LinkedListPop.prototype.pop = function () {
        if (!this.head) {
            console.log("There is no data in this linked list");
            return null;
        }
        var newTail = this.head;
        var poppedNode = this.head;
        while (poppedNode.next) {
            newTail = poppedNode;
            poppedNode = poppedNode.next;
        }
        this.tail = newTail;
        this.tail.next = null;
        this.length--;
        if (this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return poppedNode;
    };
    return LinkedListPop;
}(EXERCISE_LL_Constructor_1.LinkedList));
function test() {
    var _a, _b, _c;
    var myLinkedList = new LinkedListPop(1);
    myLinkedList.push(2);
    // (2) Items in LL - Returns 2 Node
    if (myLinkedList !== null && myLinkedList.length !== 0) {
        console.log('val: ', (_a = myLinkedList.pop()) === null || _a === void 0 ? void 0 : _a.value);
        myLinkedList.getLength();
    }
    else {
        console.log("null");
    }
    // (1) Item in LL - Returns 1 Node
    if (myLinkedList.length !== 0) {
        console.log('val: ', (_b = myLinkedList.pop()) === null || _b === void 0 ? void 0 : _b.value);
        myLinkedList.getLength();
    }
    else {
        console.log("null");
    }
    // (0) Items in LL - Returns null
    if (myLinkedList.length !== 0) {
        console.log('val: ', (_c = myLinkedList.pop()) === null || _c === void 0 ? void 0 : _c.value);
        myLinkedList.getLength();
    }
    else {
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
