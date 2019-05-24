#!/usr/bin/env python3
import itertools
import re
ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
	# Author = "Ria Gupta"
	

	def __init__ (self, vertices, edges):
		"""
		Initializes object for the class Graph

		Args:
			vertices: List of integers specifying vertices in graph
			edges: List of 2-tuples specifying edges in graph
		"""

		self.vertices = vertices
		
		ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
		
		self.edges    = ordered_edges
		
		self.validate()

	def validate(self):
		"""
		Validates if Graph if valid or not

		Raises:
			Exception if:
				- Name is empty or not a string
				- Email is empty or not a string
				- Roll Number is not in correct format
				- vertices contains duplicates
				- edges contain duplicates
				- any endpoint of an edge is not in vertices
		"""

		
		if not all([isinstance(node, int) for node in self.vertices]):
			raise Exception("All vertices should be integers")

		elif len(self.vertices) != len(set(self.vertices)):
			duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

			raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

		edge_vertices = list(set(itertools.chain(*self.edges)))

		if not all([node in self.vertices for node in edge_vertices]):
			raise Exception("All endpoints of edges must belong in vertices")

		if len(self.edges) != len(set(self.edges)):
			duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

			raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

	def create(self,vertices,edges):
		lvertices={}
		for p in range(len(vertices)):
			key=[]
				
			for i in range(len(edges)):
				for j in range(len(edges[i])):
					if vertices[p] == edges[i][j]:
						key.append(edges[i])

				
			keys=[]
			for i in key:
				for j in i:
					if j not in keys:
						keys.append(j)
					if j==vertices[p]:
						keys.remove(j)


			lvertices[vertices[p]]=keys
		return lvertices


	def min_dist(self, start_node, end_node):
		'''
		Finds minimum distance between start_node and end_node

		Args:
			start_node: Vertex to find distance from
			end_node: Vertex to find distance to

		Returns:
			An integer denoting minimum distance between start_node
			and end_node
		'''
		lvertices=graph.create(vertices,edges)
		queue=[]
		visited=[]
		distance={}


		if queue==[]:
			queue.append(list(lvertices.keys())[start_node-1])
			distance[start_node]=0


		for i in queue:     
			for j in lvertices[i]:
				if j not in visited and j not in queue:
					queue.append(j)
					distance[j]=distance[i]+1
			visited.append(i)
		f_queue=[]
		for p in queue:
			if p not in visited:
				f_queue.append(p)

		for i in distance:
			if i==end_node:
				dist=distance[i]
		return dist


		raise NotImplementedError

	def all_shortest_paths(self,start_node, end_node):
		"""
		Finds all shortest paths between 

		
		start_node and end_node


		Args:
			start_node: Starting node for paths
			end_node: Destination node for paths

		Returns:
			A list of path, where each path is a list of integers.
		"""
		lvertices=graph.create(vertices,edges)
		dist=graph.min_dist(start_node,end_node)
		paths=graph.all_paths(node=start_node,destination=end_node,dist=dist,path=[])
		formatting=graph.formatting(paths)
		return formatting


		raise NotImplementedError

	def all_paths(self,node, destination, dist, path):
		"""
		Finds all paths from node to destination with length = dist

		Args:
			node: Node to find path from
			destination: Node to reach
			dist: Allowed distance of path
			path: path already traversed

		Returns:
			List of path, where each path is list ending on destination

			Returns None if there no paths
		"""

		lvertices=graph.create(vertices,edges)
		path=path+[node]
		if len(path) ==dist+1:
			if node==destination:
				return path
			else:
				return None

		my_paths=[]
		for next_node in lvertices[node]:
			if next_node not in path:
				returned_paths=graph.all_paths(next_node,destination,dist, path)

				if returned_paths!= None:
					my_paths=my_paths+[returned_paths]

		if my_paths!=[]:
			return my_paths
		else:
			return None

		raise NotImplementedError



	def formatting(self,paths):
		list_out=''
		str_out1=''
		str_out2=''
		str_out3=''

		for i in paths:
			while not isinstance(i,int):
				if(isinstance(i[0],int)):
					break
				i = i[0]
			for j in i:
				if(isinstance(j,int)):
					list_out=list_out+str(j)
		
		return(list_out)



	def betweenness_centrality(self,node):


		"""	Find betweenness centrality of the given node
		 
			Args:
			node: Node to find betweenness centrality of.
		 
			Returns:
			Single floating point number, denoting betweenness centrality
			 of the given node"""
		previous=[]
		
		for i in vertices:
			for j in vertices:
				if i!=j and i!=node and j!=node:
					pre=[i,j]
					if [j,i] not in previous:
						previous.append(pre)

		
		total_no_min_paths=[]
		no_min_paths_through_node=[]
		
		Y=[]

		for i in previous:
				
			list_out=graph.all_shortest_paths(i[0],i[1])
			dist=graph.min_dist(i[0],i[1])
			

			u=len(list_out)
			l=[]
			a=0
			if u>(dist+1):
				x=u//(dist+1)
				for p in range(x):
					l.append(list_out[:(dist+1)])
					if str(node) in list_out[:(dist+1)]:
						a+=1
					list_out=list_out[dist+1:]
			else:
				l.append(list_out)
				if str(node) in list_out:
					a+=1
			Y.append(a)

			total_no_min_paths.append(len(l))

		bc=[]
		for i in range(len(Y)):
			p=int(Y[i])/int(total_no_min_paths[i])
			bc.append(p)
		bc_score=sum(bc)
		n=max(vertices)
		q=((n-1)*(n-2))/2
		standardized_bc=bc_score/q
		# print(standardized_bc)
		return standardized_bc
		raise NotImplementedError




		
		
	def top_k_betweenness_centrality(self):
		
		"""Find top k nodes based on highest equal betweenness centrality.

		
		Returns:
			List a integer, denoting top k nodes based on betweenness
			centrality."""

		node=vertices
		w=[]
		maximum=[]
		ty={}
		for i in node:
			standardized_bc=graph.betweenness_centrality(i)
			
			ty[i]=standardized_bc
			w.append(standardized_bc)

		max_sbc=list(ty.values())[0]
		for k in range(len(list(ty.values()))):
			if list(ty.values())[k]>max_sbc:
				max_sbc=ty[k]


		# print(max_sbc)	# here max_sbc is the value of standardized Betweeness Centrality 
		for i in ty:
			if ty[i]==max_sbc:
				maximum.append(i)
		
		return maximum
		raise NotImplementedError

if __name__ == "__main__":
	vertices = [1, 2, 3, 4, 5, 6]
	edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6), (3,6)]

	graph = Graph(vertices, edges)

	d = graph.top_k_betweenness_centrality()
	print(d)
