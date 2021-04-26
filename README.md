# [Algoritmos e Estruturas de Dados 2020 2021](https://elearning.ual.pt/course/view.php?id=1787) - [UAL](https://autonoma.pt/)

## Laboratório 3

O objetivo deste laboratório é produzir duas implementações do *tipo abstrato de dados* (ADT) **Lista**, com os respetivos iteradores.

Este enunciado é acompanhado por um conjunto de ADTs, implementações de nós simples e duplos (`aed_ds/lists/nodes.py`), e um conjunto de exceções (`aed_ds/exceptions.py`).

Vai ser necessário criar os seguintes módulos:

- **`aed_ds/lists/singly_linked_list.py`**, que vai ter a classe `SinglyLinkedList`, com a implementação da lista simplesmente ligada, de acordo com o ADT `List`, em `aed_ds/lists/adt_list.py`
- **`aed_ds/lists/doubly_linked_list.py`**, que vai ter a classe `DoublyLinkedList`, com a implementação da lista duplamente ligada, de acordo com o ADT `List`, em `aed_ds/lists/adt_list.py`
- **`aed_ds/lists/singly_linked_list_iterator.py`**, que vai ter a classe `SinglyLinkedListIterator`, com a implementação do iterador da lista simplesmente ligada, de acordo com o ADT `Iterator`, em `aed_ds/iterator.py`
- **`aed_ds/lists/doubly_linked_list_iterator.py`**, que vai ter a classe `DoublyLinkedListIterator`, com a implementação do iterator da lista duplamente ligada, de acordo com o ADT `Iterator`, em `aed_ds/iterator.py`

A acompanhar o código segue também uma bateria de testes:

- `tests/lists/test_singly_linked_list.py` que testa a classe `SinglyLinkedList`
- `tests/lists/test_doubly_linked_list.py` que testa a classe `DoubleLinkedList`
- `tests/lists/test_singly_linked_list_iterator.py` que testa a classe `SinglyLinkedListIterator`
- `tests/lists/test_doubly_linked_list_iterator.py` que testa a classe `DoublyLinkedListIterator`

O laboratório é considerado completo quando todos os testes estiverem passados.

Os testes não são necessariamente exaustivos, pelo que o grupo de trabalho pode *acrescentar* testes, mas não pode alterar os que foram distribuídos.

Os testes pode ser executados de várias formas:

- Todos os testes de uma classe
  - E.g., `python -m unittest test.singly_linked_list`
- Apenas um teste de uma classe
  - E.g., `python -m unittest test.singly_linked_list.SinglyLinkedList.test_is_empty`
- Todos os ficheiros de teste
  - `python -m unittest discover tests`

## Datas

| Evento                        | Data                 |
| ----------------------------- | -------------------- |
| Disponibilização de enunciado | 26/04/2021           |
| Entrega                       | 09/05/2021, 23:59:59 |

## Regras

- O trabalho deve ser realizado em grupo, previamente registado no *e-learning*.
- O código produzido deverá estar disponível no repositório GitHub gerado pelo GitHub Classroom.
  - Podem ser criados vários *branches*, de acordo com o organização que o grupo de trabalho considerar mais conveniente.
  - Deve sempre existir um *branch* `main`, onde a versão final deverá ficar disponível.

## Entrega
A versão final do trabalho deve estar disponível na *branch* `main` do repositório até à hora limite de entrega. <span style="color: red">Não serão considerados *commits* com data posterior à data limite.</span>

A entrega deve também ser feita no *e-learning*, num ficheiro `zip` com todo o projeto.
