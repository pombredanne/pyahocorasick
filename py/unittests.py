
from pyahocorasick import Trie


def test_EmptyTrieShouldNotContainsAnyWords():
    t = Trie()
    assert len(t) ==0


def test_AddedWordShouldBeCountedAndAvailableForRetrieval():
    t = Trie()
    t.add('python', 'value')
    assert len(t)== 1
    assert t.get('python')== 'value'


def test_AddingExistingWordShouldReplaceAssociatedValue():
    t = Trie()
    t.add('python', 'value')
    assert len(t) ==1
    assert t.get('python') =='value'

    t.add('python', 'other')
    assert len(t) ==1
    assert t.get('python') =='other'


def test_GetUnknowWordWithoutDefaultValueShouldRaiseException():
    t = Trie()
    try:
        t.get('python')
    except KeyError:
        pass


def test_GetUnknowWordWithDefaultValueShouldReturnDefault():
    t = Trie()
    assert t.get('python', 'default') =='default'


def test_ExistShouldDetectAddedWords():
    t = Trie()
    t.add('python', 'value')
    t.add('ada', 'value')

    assert t.exists('python')
    assert t.exists('ada')


def test_ExistShouldReturnFailOnUnknownWord():
    t = Trie()
    t.add('python', 'value')

    assert not t.exists('ada')


def test_MatchShouldDetecAllPrefixesIncludingWord():
    t = Trie()
    t.add('python', 'value')
    t.add('ada', 'value')

    assert t.match('a')
    assert t.match('ad')
    assert t.match('ada')

    assert t.match('p')
    assert t.match('py')
    assert t.match('pyt')
    assert t.match('pyth')
    assert t.match('pytho')
    assert t.match('python')


def test_iteritems_ShouldReturnAllItemsAlreadyAddedToTheTrie():
    t = Trie()
    t.add('python', 1)
    t.add('ada', 2)
    t.add('perl', 3)
    t.add('pascal', 4)
    t.add('php', 5)

    result = [(''.join(k), v) for k, v in t.iteritems()]
    assert len(result) == 5
    assert ('python', 1) in result
    assert ('ada', 2) in result
    assert ('perl', 3) in result
    assert ('pascal', 4) in result
    assert ('php', 5) in result


def test_iterkeys_ShouldReturnAllKeysAlreadyAddedToTheTrie():
    t = Trie()
    t.add('python', 1)
    t.add('ada', 2)
    t.add('perl', 3)
    t.add('pascal', 4)
    t.add('php', 5)

    result = [''.join(k) for k  in t.iterkeys()]
    assert len(result), 5
    assert 'python' in result
    assert 'ada' in result
    assert 'perl' in result
    assert 'pascal' in result
    assert 'php' in result


def test_itervalues_ShouldReturnAllValuesAlreadyAddedToTheTrie():
    t = Trie()
    t.add('python', 1)
    t.add('ada', 2)
    t.add('perl', 3)
    t.add('pascal', 4)
    t.add('php', 5)

    result = list(t.itervalues())
    assert len(result) ==5
    assert 1 in result
    assert 2 in result
    assert 3 in result
    assert 4 in result
    assert 5 in result


def get_test_automaton():
    words = 'he her hers his she hi him man himan'.split()
    t = Trie();
    for w in words:
        t.add(w, w)
    t.make_automaton()
    return t


def test_search_should_match_all_strings():
    words = 'he her hers his she hi him man himan'.split()
    t = Trie();
    for w in words:
        t.add(w, w)
    t.make_automaton()

    test_string = 'he she himan'
    result = list(t.search(test_string))

    # there are 5 matching positions
    assert len(result) ==5

    # result should have be valid, i.e. returned position and substring
    # must match substring from test string
    for end_index, strings in result:
        for s in strings:
            n = len(s)
            assert s, test_string[end_index - n + 1 : end_index + 1]
