#!/usr/bin/python3
def multiple_returns(sentence):
    m_t = ()
    if len(sentence) == 0:
        m_t = 0, "None"
    else:
        m_t = len(sentence), sentence[0]
    return m_t
