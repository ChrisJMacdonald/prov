# Generated from PROV_N.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PROV_NParser import PROV_NParser
else:
    from PROV_NParser import PROV_NParser

# This class defines a complete generic visitor for a parse tree produced by PROV_NParser.

class PROV_NVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PROV_NParser#document.
    def visitDocument(self, ctx:PROV_NParser.DocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#namespaceDeclarations.
    def visitNamespaceDeclarations(self, ctx:PROV_NParser.NamespaceDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#defaultNamespaceDeclaration.
    def visitDefaultNamespaceDeclaration(self, ctx:PROV_NParser.DefaultNamespaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#namespaceDeclaration.
    def visitNamespaceDeclaration(self, ctx:PROV_NParser.NamespaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#namespace.
    def visitNamespace(self, ctx:PROV_NParser.NamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#bundle.
    def visitBundle(self, ctx:PROV_NParser.BundleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#identifier.
    def visitIdentifier(self, ctx:PROV_NParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#expression.
    def visitExpression(self, ctx:PROV_NParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#entityExpression.
    def visitEntityExpression(self, ctx:PROV_NParser.EntityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#optionalAttributeValuePairs.
    def visitOptionalAttributeValuePairs(self, ctx:PROV_NParser.OptionalAttributeValuePairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#attributeValuePairs.
    def visitAttributeValuePairs(self, ctx:PROV_NParser.AttributeValuePairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#attributeValuePair.
    def visitAttributeValuePair(self, ctx:PROV_NParser.AttributeValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#attribute.
    def visitAttribute(self, ctx:PROV_NParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#literal.
    def visitLiteral(self, ctx:PROV_NParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#typedLiteral.
    def visitTypedLiteral(self, ctx:PROV_NParser.TypedLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#datatype.
    def visitDatatype(self, ctx:PROV_NParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#convenienceNotation.
    def visitConvenienceNotation(self, ctx:PROV_NParser.ConvenienceNotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#activityExpression.
    def visitActivityExpression(self, ctx:PROV_NParser.ActivityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#timeOrMarker.
    def visitTimeOrMarker(self, ctx:PROV_NParser.TimeOrMarkerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#time.
    def visitTime(self, ctx:PROV_NParser.TimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#generationExpression.
    def visitGenerationExpression(self, ctx:PROV_NParser.GenerationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#optionalIdentifier.
    def visitOptionalIdentifier(self, ctx:PROV_NParser.OptionalIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#identifierOrMarker.
    def visitIdentifierOrMarker(self, ctx:PROV_NParser.IdentifierOrMarkerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#eIdentifier.
    def visitEIdentifier(self, ctx:PROV_NParser.EIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#eIdentifierOrMarker.
    def visitEIdentifierOrMarker(self, ctx:PROV_NParser.EIdentifierOrMarkerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#aIdentifierOrMarker.
    def visitAIdentifierOrMarker(self, ctx:PROV_NParser.AIdentifierOrMarkerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#aIdentifier.
    def visitAIdentifier(self, ctx:PROV_NParser.AIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#agIdentifierOrMarker.
    def visitAgIdentifierOrMarker(self, ctx:PROV_NParser.AgIdentifierOrMarkerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#agIdentifier.
    def visitAgIdentifier(self, ctx:PROV_NParser.AgIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#cIdentifier.
    def visitCIdentifier(self, ctx:PROV_NParser.CIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#gIdentifier.
    def visitGIdentifier(self, ctx:PROV_NParser.GIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#gIdentifierOrMarker.
    def visitGIdentifierOrMarker(self, ctx:PROV_NParser.GIdentifierOrMarkerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#uIdentifier.
    def visitUIdentifier(self, ctx:PROV_NParser.UIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#uIdentifierOrMarker.
    def visitUIdentifierOrMarker(self, ctx:PROV_NParser.UIdentifierOrMarkerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#usageExpression.
    def visitUsageExpression(self, ctx:PROV_NParser.UsageExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#startExpression.
    def visitStartExpression(self, ctx:PROV_NParser.StartExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#endExpression.
    def visitEndExpression(self, ctx:PROV_NParser.EndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#invalidationExpression.
    def visitInvalidationExpression(self, ctx:PROV_NParser.InvalidationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#communicationExpression.
    def visitCommunicationExpression(self, ctx:PROV_NParser.CommunicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#agentExpression.
    def visitAgentExpression(self, ctx:PROV_NParser.AgentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#associationExpression.
    def visitAssociationExpression(self, ctx:PROV_NParser.AssociationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#attributionExpression.
    def visitAttributionExpression(self, ctx:PROV_NParser.AttributionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#delegationExpression.
    def visitDelegationExpression(self, ctx:PROV_NParser.DelegationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#derivationExpression.
    def visitDerivationExpression(self, ctx:PROV_NParser.DerivationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#influenceExpression.
    def visitInfluenceExpression(self, ctx:PROV_NParser.InfluenceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#alternateExpression.
    def visitAlternateExpression(self, ctx:PROV_NParser.AlternateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#specializationExpression.
    def visitSpecializationExpression(self, ctx:PROV_NParser.SpecializationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#membershipExpression.
    def visitMembershipExpression(self, ctx:PROV_NParser.MembershipExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#extensibilityExpression.
    def visitExtensibilityExpression(self, ctx:PROV_NParser.ExtensibilityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#extensibilityArgument.
    def visitExtensibilityArgument(self, ctx:PROV_NParser.ExtensibilityArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PROV_NParser#extensibilityTuple.
    def visitExtensibilityTuple(self, ctx:PROV_NParser.ExtensibilityTupleContext):
        return self.visitChildren(ctx)



del PROV_NParser