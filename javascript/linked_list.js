'use strict'

class Node {
    constructor(data=null, next=null){
        this.data = data
        this.next = next
    }
}

class LinkedList {
    constructor(iterable=null){
        this.head = null
        this._count = 0
        if(Array.isArray(iterable)){
            iterable.forEach(x => this.push(x))
        }
    }

  push(val) {
      this.head = new Node(val, this.head)
      this._count ++
  }

  pop() {
      if(this.head === null) {
          return 'Cannot pop from an empty list.'
      }
      let popNode = this.head
      this.head = popNode.next
      this._count --
      return popNode.data
  }

  size() {
      return this._count
  }

  search() {
      let current = this.head
      while(current){
          if(current.data === val){
              return current
            }
          else{
          current = current.next
          if(current === null){
              return 'Your node is not in the list.'
          }
      }
  }
}

  display(){
      if(this._count > 0){
          let display_str = '('
          let current = this.head
          while(current){
              if(current.next){
                  display_str = display_str + current.data + ', '
              }
              else {
                  display_str = display_str + current.data + ')'
                  return display_str
              }
              current = current.next
          }
      }
      else {
          return '()'
      }
  }

  remove(node) {
      let current = this.head
      let previous = null
      while(current){
          if(current === node){
              if(current === this.head){
                  this.head = current.next
                  this._count --
              }
              else {
                  if(current.next === null){
                      previous.next = null
                  }
                  else{
                      previous.next = current.next
                  }
                  this._count --
              }
              break
          }
          else {
              previous = current
              current = current.next
          }

      }
      return 'Your node is not in this list.'
    }
}
module.exports = {LinkedList, Node}
