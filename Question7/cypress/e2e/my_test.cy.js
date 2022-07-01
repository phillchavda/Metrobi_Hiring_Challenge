
/// <reference types="cypress" />

// add, delete, submit and edit items

it('google test', function(){
  cy.visit('http://localhost:3000/react-todo-project')
  cy.get(".input-text").type('My first note {enter}')
  cy.wait(1000)
  cy.get(".input-text").type('My second note {enter}')
  cy.wait(1000)
  cy.get(".input-text").type('My third note {enter}')
  cy.wait(1000)
  cy.get(':nth-child(1) > div > .TodoItem_checkbox__2Jrs8').type('{enter}')
  cy.wait(1000)
  cy.get(':nth-child(2) > div > button').click()
  cy.wait(2000)
  cy.get('ul > :nth-child(2) > div').dblclick()
  cy.wait(1000)
  cy.get(':nth-child(2) > .TodoItem_textInput__t35cu').type('{selectall}{backspace}My edited note{enter}')
})