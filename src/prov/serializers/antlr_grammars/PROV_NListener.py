# Generated from /home/marcel/workspace/antlr4/PROV_N.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PROV_NParser import PROV_NParser
else:
    from PROV_NParser import PROV_NParser

# This class defines a complete listener for a parse tree produced by PROV_NParser.
class PROV_NListener(ParseTreeListener):

    # Enter a parse tree produced by PROV_NParser#document.
    def enterDocument(self, ctx:PROV_NParser.DocumentContext):
        pass

    # Exit a parse tree produced by PROV_NParser#document.
    def exitDocument(self, ctx:PROV_NParser.DocumentContext):
        pass


    # Enter a parse tree produced by PROV_NParser#namespaceDeclarations.
    def enterNamespaceDeclarations(self, ctx:PROV_NParser.NamespaceDeclarationsContext):
        pass

    # Exit a parse tree produced by PROV_NParser#namespaceDeclarations.
    def exitNamespaceDeclarations(self, ctx:PROV_NParser.NamespaceDeclarationsContext):
        pass


    # Enter a parse tree produced by PROV_NParser#defaultNamespaceDeclaration.
    def enterDefaultNamespaceDeclaration(self, ctx:PROV_NParser.DefaultNamespaceDeclarationContext):
        pass

    # Exit a parse tree produced by PROV_NParser#defaultNamespaceDeclaration.
    def exitDefaultNamespaceDeclaration(self, ctx:PROV_NParser.DefaultNamespaceDeclarationContext):
        pass


    # Enter a parse tree produced by PROV_NParser#namespaceDeclaration.
    def enterNamespaceDeclaration(self, ctx:PROV_NParser.NamespaceDeclarationContext):
        pass

    # Exit a parse tree produced by PROV_NParser#namespaceDeclaration.
    def exitNamespaceDeclaration(self, ctx:PROV_NParser.NamespaceDeclarationContext):
        pass


    # Enter a parse tree produced by PROV_NParser#namespace.
    def enterNamespace(self, ctx:PROV_NParser.NamespaceContext):
        pass

    # Exit a parse tree produced by PROV_NParser#namespace.
    def exitNamespace(self, ctx:PROV_NParser.NamespaceContext):
        pass


    # Enter a parse tree produced by PROV_NParser#bundle.
    def enterBundle(self, ctx:PROV_NParser.BundleContext):
        pass

    # Exit a parse tree produced by PROV_NParser#bundle.
    def exitBundle(self, ctx:PROV_NParser.BundleContext):
        pass


    # Enter a parse tree produced by PROV_NParser#identifier.
    def enterIdentifier(self, ctx:PROV_NParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PROV_NParser#identifier.
    def exitIdentifier(self, ctx:PROV_NParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PROV_NParser#expression.
    def enterExpression(self, ctx:PROV_NParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#expression.
    def exitExpression(self, ctx:PROV_NParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#entityExpression.
    def enterEntityExpression(self, ctx:PROV_NParser.EntityExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#entityExpression.
    def exitEntityExpression(self, ctx:PROV_NParser.EntityExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#optionalAttributeValuePairs.
    def enterOptionalAttributeValuePairs(self, ctx:PROV_NParser.OptionalAttributeValuePairsContext):
        pass

    # Exit a parse tree produced by PROV_NParser#optionalAttributeValuePairs.
    def exitOptionalAttributeValuePairs(self, ctx:PROV_NParser.OptionalAttributeValuePairsContext):
        pass


    # Enter a parse tree produced by PROV_NParser#attributeValuePairs.
    def enterAttributeValuePairs(self, ctx:PROV_NParser.AttributeValuePairsContext):
        pass

    # Exit a parse tree produced by PROV_NParser#attributeValuePairs.
    def exitAttributeValuePairs(self, ctx:PROV_NParser.AttributeValuePairsContext):
        pass


    # Enter a parse tree produced by PROV_NParser#attributeValuePair.
    def enterAttributeValuePair(self, ctx:PROV_NParser.AttributeValuePairContext):
        pass

    # Exit a parse tree produced by PROV_NParser#attributeValuePair.
    def exitAttributeValuePair(self, ctx:PROV_NParser.AttributeValuePairContext):
        pass


    # Enter a parse tree produced by PROV_NParser#attribute.
    def enterAttribute(self, ctx:PROV_NParser.AttributeContext):
        pass

    # Exit a parse tree produced by PROV_NParser#attribute.
    def exitAttribute(self, ctx:PROV_NParser.AttributeContext):
        pass


    # Enter a parse tree produced by PROV_NParser#literal.
    def enterLiteral(self, ctx:PROV_NParser.LiteralContext):
        pass

    # Exit a parse tree produced by PROV_NParser#literal.
    def exitLiteral(self, ctx:PROV_NParser.LiteralContext):
        pass


    # Enter a parse tree produced by PROV_NParser#typedLiteral.
    def enterTypedLiteral(self, ctx:PROV_NParser.TypedLiteralContext):
        pass

    # Exit a parse tree produced by PROV_NParser#typedLiteral.
    def exitTypedLiteral(self, ctx:PROV_NParser.TypedLiteralContext):
        pass


    # Enter a parse tree produced by PROV_NParser#datatype.
    def enterDatatype(self, ctx:PROV_NParser.DatatypeContext):
        pass

    # Exit a parse tree produced by PROV_NParser#datatype.
    def exitDatatype(self, ctx:PROV_NParser.DatatypeContext):
        pass


    # Enter a parse tree produced by PROV_NParser#convenienceNotation.
    def enterConvenienceNotation(self, ctx:PROV_NParser.ConvenienceNotationContext):
        pass

    # Exit a parse tree produced by PROV_NParser#convenienceNotation.
    def exitConvenienceNotation(self, ctx:PROV_NParser.ConvenienceNotationContext):
        pass


    # Enter a parse tree produced by PROV_NParser#activityExpression.
    def enterActivityExpression(self, ctx:PROV_NParser.ActivityExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#activityExpression.
    def exitActivityExpression(self, ctx:PROV_NParser.ActivityExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#timeOrMarker.
    def enterTimeOrMarker(self, ctx:PROV_NParser.TimeOrMarkerContext):
        pass

    # Exit a parse tree produced by PROV_NParser#timeOrMarker.
    def exitTimeOrMarker(self, ctx:PROV_NParser.TimeOrMarkerContext):
        pass


    # Enter a parse tree produced by PROV_NParser#time.
    def enterTime(self, ctx:PROV_NParser.TimeContext):
        pass

    # Exit a parse tree produced by PROV_NParser#time.
    def exitTime(self, ctx:PROV_NParser.TimeContext):
        pass


    # Enter a parse tree produced by PROV_NParser#generationExpression.
    def enterGenerationExpression(self, ctx:PROV_NParser.GenerationExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#generationExpression.
    def exitGenerationExpression(self, ctx:PROV_NParser.GenerationExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#optionalIdentifier.
    def enterOptionalIdentifier(self, ctx:PROV_NParser.OptionalIdentifierContext):
        pass

    # Exit a parse tree produced by PROV_NParser#optionalIdentifier.
    def exitOptionalIdentifier(self, ctx:PROV_NParser.OptionalIdentifierContext):
        pass


    # Enter a parse tree produced by PROV_NParser#identifierOrMarker.
    def enterIdentifierOrMarker(self, ctx:PROV_NParser.IdentifierOrMarkerContext):
        pass

    # Exit a parse tree produced by PROV_NParser#identifierOrMarker.
    def exitIdentifierOrMarker(self, ctx:PROV_NParser.IdentifierOrMarkerContext):
        pass


    # Enter a parse tree produced by PROV_NParser#eIdentifier.
    def enterEIdentifier(self, ctx:PROV_NParser.EIdentifierContext):
        pass

    # Exit a parse tree produced by PROV_NParser#eIdentifier.
    def exitEIdentifier(self, ctx:PROV_NParser.EIdentifierContext):
        pass


    # Enter a parse tree produced by PROV_NParser#eIdentifierOrMarker.
    def enterEIdentifierOrMarker(self, ctx:PROV_NParser.EIdentifierOrMarkerContext):
        pass

    # Exit a parse tree produced by PROV_NParser#eIdentifierOrMarker.
    def exitEIdentifierOrMarker(self, ctx:PROV_NParser.EIdentifierOrMarkerContext):
        pass


    # Enter a parse tree produced by PROV_NParser#aIdentifierOrMarker.
    def enterAIdentifierOrMarker(self, ctx:PROV_NParser.AIdentifierOrMarkerContext):
        pass

    # Exit a parse tree produced by PROV_NParser#aIdentifierOrMarker.
    def exitAIdentifierOrMarker(self, ctx:PROV_NParser.AIdentifierOrMarkerContext):
        pass


    # Enter a parse tree produced by PROV_NParser#aIdentifier.
    def enterAIdentifier(self, ctx:PROV_NParser.AIdentifierContext):
        pass

    # Exit a parse tree produced by PROV_NParser#aIdentifier.
    def exitAIdentifier(self, ctx:PROV_NParser.AIdentifierContext):
        pass


    # Enter a parse tree produced by PROV_NParser#agIdentifierOrMarker.
    def enterAgIdentifierOrMarker(self, ctx:PROV_NParser.AgIdentifierOrMarkerContext):
        pass

    # Exit a parse tree produced by PROV_NParser#agIdentifierOrMarker.
    def exitAgIdentifierOrMarker(self, ctx:PROV_NParser.AgIdentifierOrMarkerContext):
        pass


    # Enter a parse tree produced by PROV_NParser#agIdentifier.
    def enterAgIdentifier(self, ctx:PROV_NParser.AgIdentifierContext):
        pass

    # Exit a parse tree produced by PROV_NParser#agIdentifier.
    def exitAgIdentifier(self, ctx:PROV_NParser.AgIdentifierContext):
        pass


    # Enter a parse tree produced by PROV_NParser#cIdentifier.
    def enterCIdentifier(self, ctx:PROV_NParser.CIdentifierContext):
        pass

    # Exit a parse tree produced by PROV_NParser#cIdentifier.
    def exitCIdentifier(self, ctx:PROV_NParser.CIdentifierContext):
        pass


    # Enter a parse tree produced by PROV_NParser#gIdentifier.
    def enterGIdentifier(self, ctx:PROV_NParser.GIdentifierContext):
        pass

    # Exit a parse tree produced by PROV_NParser#gIdentifier.
    def exitGIdentifier(self, ctx:PROV_NParser.GIdentifierContext):
        pass


    # Enter a parse tree produced by PROV_NParser#gIdentifierOrMarker.
    def enterGIdentifierOrMarker(self, ctx:PROV_NParser.GIdentifierOrMarkerContext):
        pass

    # Exit a parse tree produced by PROV_NParser#gIdentifierOrMarker.
    def exitGIdentifierOrMarker(self, ctx:PROV_NParser.GIdentifierOrMarkerContext):
        pass


    # Enter a parse tree produced by PROV_NParser#uIdentifier.
    def enterUIdentifier(self, ctx:PROV_NParser.UIdentifierContext):
        pass

    # Exit a parse tree produced by PROV_NParser#uIdentifier.
    def exitUIdentifier(self, ctx:PROV_NParser.UIdentifierContext):
        pass


    # Enter a parse tree produced by PROV_NParser#uIdentifierOrMarker.
    def enterUIdentifierOrMarker(self, ctx:PROV_NParser.UIdentifierOrMarkerContext):
        pass

    # Exit a parse tree produced by PROV_NParser#uIdentifierOrMarker.
    def exitUIdentifierOrMarker(self, ctx:PROV_NParser.UIdentifierOrMarkerContext):
        pass


    # Enter a parse tree produced by PROV_NParser#usageExpression.
    def enterUsageExpression(self, ctx:PROV_NParser.UsageExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#usageExpression.
    def exitUsageExpression(self, ctx:PROV_NParser.UsageExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#startExpression.
    def enterStartExpression(self, ctx:PROV_NParser.StartExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#startExpression.
    def exitStartExpression(self, ctx:PROV_NParser.StartExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#endExpression.
    def enterEndExpression(self, ctx:PROV_NParser.EndExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#endExpression.
    def exitEndExpression(self, ctx:PROV_NParser.EndExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#invalidationExpression.
    def enterInvalidationExpression(self, ctx:PROV_NParser.InvalidationExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#invalidationExpression.
    def exitInvalidationExpression(self, ctx:PROV_NParser.InvalidationExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#communicationExpression.
    def enterCommunicationExpression(self, ctx:PROV_NParser.CommunicationExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#communicationExpression.
    def exitCommunicationExpression(self, ctx:PROV_NParser.CommunicationExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#agentExpression.
    def enterAgentExpression(self, ctx:PROV_NParser.AgentExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#agentExpression.
    def exitAgentExpression(self, ctx:PROV_NParser.AgentExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#associationExpression.
    def enterAssociationExpression(self, ctx:PROV_NParser.AssociationExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#associationExpression.
    def exitAssociationExpression(self, ctx:PROV_NParser.AssociationExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#attributionExpression.
    def enterAttributionExpression(self, ctx:PROV_NParser.AttributionExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#attributionExpression.
    def exitAttributionExpression(self, ctx:PROV_NParser.AttributionExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#delegationExpression.
    def enterDelegationExpression(self, ctx:PROV_NParser.DelegationExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#delegationExpression.
    def exitDelegationExpression(self, ctx:PROV_NParser.DelegationExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#derivationExpression.
    def enterDerivationExpression(self, ctx:PROV_NParser.DerivationExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#derivationExpression.
    def exitDerivationExpression(self, ctx:PROV_NParser.DerivationExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#influenceExpression.
    def enterInfluenceExpression(self, ctx:PROV_NParser.InfluenceExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#influenceExpression.
    def exitInfluenceExpression(self, ctx:PROV_NParser.InfluenceExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#alternateExpression.
    def enterAlternateExpression(self, ctx:PROV_NParser.AlternateExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#alternateExpression.
    def exitAlternateExpression(self, ctx:PROV_NParser.AlternateExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#specializationExpression.
    def enterSpecializationExpression(self, ctx:PROV_NParser.SpecializationExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#specializationExpression.
    def exitSpecializationExpression(self, ctx:PROV_NParser.SpecializationExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#membershipExpression.
    def enterMembershipExpression(self, ctx:PROV_NParser.MembershipExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#membershipExpression.
    def exitMembershipExpression(self, ctx:PROV_NParser.MembershipExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#extensibilityExpression.
    def enterExtensibilityExpression(self, ctx:PROV_NParser.ExtensibilityExpressionContext):
        pass

    # Exit a parse tree produced by PROV_NParser#extensibilityExpression.
    def exitExtensibilityExpression(self, ctx:PROV_NParser.ExtensibilityExpressionContext):
        pass


    # Enter a parse tree produced by PROV_NParser#extensibilityArgument.
    def enterExtensibilityArgument(self, ctx:PROV_NParser.ExtensibilityArgumentContext):
        pass

    # Exit a parse tree produced by PROV_NParser#extensibilityArgument.
    def exitExtensibilityArgument(self, ctx:PROV_NParser.ExtensibilityArgumentContext):
        pass


    # Enter a parse tree produced by PROV_NParser#extensibilityTuple.
    def enterExtensibilityTuple(self, ctx:PROV_NParser.ExtensibilityTupleContext):
        pass

    # Exit a parse tree produced by PROV_NParser#extensibilityTuple.
    def exitExtensibilityTuple(self, ctx:PROV_NParser.ExtensibilityTupleContext):
        pass


