#  # PROV record constants - PROV-DM

# Built-in namespaces
from prov.identifier import Namespace

XSD = Namespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
PROV = Namespace('prov', 'http://www.w3.org/ns/prov#')

#  C1. Entities/Activities
PROV_REC_ENTITY = 1
PROV_REC_ACTIVITY = 2
PROV_REC_GENERATION = 11
PROV_REC_USAGE = 12
PROV_REC_COMMUNICATION = 13
PROV_REC_START = 14
PROV_REC_END = 15
PROV_REC_INVALIDATION = 16

#  C2. Derivations
PROV_REC_DERIVATION = 21

#  C3. Agents/Responsibility
PROV_REC_AGENT = 3
PROV_REC_ATTRIBUTION = 31
PROV_REC_ASSOCIATION = 32
PROV_REC_DELEGATION = 33
PROV_REC_INFLUENCE = 34
#  C4. Bundles
PROV_REC_BUNDLE = 4  # This is the lowest value, so bundle(s) in JSON will be decoded first
#  C5. Alternate
PROV_REC_ALTERNATE = 51
PROV_REC_SPECIALIZATION = 52
PROV_REC_MENTION = 53
#  C6. Collections
PROV_REC_MEMBERSHIP = 61

PROV_RECORD_TYPES = (
    (PROV_REC_ENTITY, u'Entity'),
    (PROV_REC_ACTIVITY, u'Activity'),
    (PROV_REC_GENERATION, u'Generation'),
    (PROV_REC_USAGE, u'Usage'),
    (PROV_REC_COMMUNICATION, u'Communication'),
    (PROV_REC_START, u'Start'),
    (PROV_REC_END, u'End'),
    (PROV_REC_INVALIDATION, u'Invalidation'),
    (PROV_REC_DERIVATION, u'Derivation'),
    (PROV_REC_AGENT, u'Agent'),
    (PROV_REC_ATTRIBUTION, u'Attribution'),
    (PROV_REC_ASSOCIATION, u'Association'),
    (PROV_REC_DELEGATION, u'Delegation'),
    (PROV_REC_INFLUENCE, u'Influence'),
    (PROV_REC_BUNDLE, u'Bundle'),
    (PROV_REC_ALTERNATE, u'Alternate'),
    (PROV_REC_SPECIALIZATION, u'Specialization'),
    (PROV_REC_MENTION, u'Mention'),
    (PROV_REC_MEMBERSHIP, u'Membership'),
)

PROV_N_MAP = {
    PROV_REC_ENTITY:               u'entity',
    PROV_REC_ACTIVITY:             u'activity',
    PROV_REC_GENERATION:           u'wasGeneratedBy',
    PROV_REC_USAGE:                u'used',
    PROV_REC_COMMUNICATION:        u'wasInformedBy',
    PROV_REC_START:                u'wasStartedBy',
    PROV_REC_END:                  u'wasEndedBy',
    PROV_REC_INVALIDATION:         u'wasInvalidatedBy',
    PROV_REC_DERIVATION:           u'wasDerivedFrom',
    PROV_REC_AGENT:                u'agent',
    PROV_REC_ATTRIBUTION:          u'wasAttributedTo',
    PROV_REC_ASSOCIATION:          u'wasAssociatedWith',
    PROV_REC_DELEGATION:           u'actedOnBehalfOf',
    PROV_REC_INFLUENCE:            u'wasInfluencedBy',
    PROV_REC_ALTERNATE:            u'alternateOf',
    PROV_REC_SPECIALIZATION:       u'specializationOf',
    PROV_REC_MENTION:              u'mentionOf',
    PROV_REC_MEMBERSHIP:           u'hadMember',
    PROV_REC_BUNDLE:               u'bundle',
}

# Identifiers for PROV's attributes
PROV_ATTR_ENTITY = PROV['entity']
PROV_ATTR_ACTIVITY = PROV['activity']
PROV_ATTR_TRIGGER = PROV['trigger']
PROV_ATTR_INFORMED = PROV['informed']
PROV_ATTR_INFORMANT = PROV['informant']
PROV_ATTR_STARTER = PROV['starter']
PROV_ATTR_ENDER = PROV['ender']
PROV_ATTR_AGENT = PROV['agent']
PROV_ATTR_PLAN = PROV['plan']
PROV_ATTR_DELEGATE = PROV['delegate']
PROV_ATTR_RESPONSIBLE = PROV['responsible']
PROV_ATTR_GENERATED_ENTITY = PROV['generatedEntity']
PROV_ATTR_USED_ENTITY = PROV['usedEntity']
PROV_ATTR_GENERATION = PROV['generation']
PROV_ATTR_USAGE = PROV['usage']
PROV_ATTR_SPECIFIC_ENTITY = PROV['specificEntity']
PROV_ATTR_GENERAL_ENTITY = PROV['generalEntity']
PROV_ATTR_ALTERNATE1 = PROV['alternate1']
PROV_ATTR_ALTERNATE2 = PROV['alternate2']
PROV_ATTR_BUNDLE = PROV['bundle']
PROV_ATTR_INFLUENCEE = PROV['influencee']
PROV_ATTR_INFLUENCER = PROV['influencer']
PROV_ATTR_COLLECTION = PROV['collection']

#  Literal properties
PROV_ATTR_TIME = PROV['time']
PROV_ATTR_STARTTIME = PROV['startTime']
PROV_ATTR_ENDTIME = PROV['endTime']


PROV_ATTRIBUTE_QNAMES = {
    PROV_ATTR_ENTITY,
    PROV_ATTR_ACTIVITY,
    PROV_ATTR_TRIGGER,
    PROV_ATTR_INFORMED,
    PROV_ATTR_INFORMANT,
    PROV_ATTR_STARTER,
    PROV_ATTR_ENDER,
    PROV_ATTR_AGENT,
    PROV_ATTR_PLAN,
    PROV_ATTR_DELEGATE,
    PROV_ATTR_RESPONSIBLE,
    PROV_ATTR_GENERATED_ENTITY,
    PROV_ATTR_USED_ENTITY,
    PROV_ATTR_GENERATION,
    PROV_ATTR_USAGE,
    PROV_ATTR_SPECIFIC_ENTITY,
    PROV_ATTR_GENERAL_ENTITY,
    PROV_ATTR_ALTERNATE1,
    PROV_ATTR_ALTERNATE2,
    PROV_ATTR_BUNDLE,
    PROV_ATTR_INFLUENCEE,
    PROV_ATTR_INFLUENCER,
    PROV_ATTR_COLLECTION
}
PROV_ATTRIBUTE_LITERALS = {PROV_ATTR_TIME, PROV_ATTR_STARTTIME, PROV_ATTR_ENDTIME}
PROV_ATTRIBUTES = PROV_ATTRIBUTE_QNAMES | PROV_ATTRIBUTE_LITERALS
PROV_RECORD_ATTRIBUTES = list((attr, unicode(attr)) for attr in PROV_ATTRIBUTES)

PROV_RECORD_IDS_MAP = dict((PROV_N_MAP[rec_type_id], rec_type_id) for rec_type_id in PROV_N_MAP)
PROV_ID_ATTRIBUTES_MAP = dict((prov_id, attribute) for (prov_id, attribute) in PROV_RECORD_ATTRIBUTES)
PROV_ATTRIBUTES_ID_MAP = dict((attribute, prov_id) for (prov_id, attribute) in PROV_RECORD_ATTRIBUTES)

